#!/usr/bin/env python3
"""
FiiO M27 Manual Image Translator
Uses Gemini (Nano Banana Pro) API to translate English text in images to Japanese.
"""

import sys
import os
import time
import json
from io import BytesIO
from pathlib import Path

from google import genai
from google.genai import types
from PIL import Image

# API Configuration
API_KEY = os.environ.get("GEMINI_API_KEY", "")
PRIMARY_MODEL = "gemini-3-pro-image-preview"
FALLBACK_MODEL = "gemini-2.5-flash-image"

# Directories
BASE_DIR = Path("/Users/kenzo/claude/manual-test/output/m27-manual-ja-v3/images")

# Prompts
UI_PROMPT = """この画像はFiiO M27デジタルオーディオプレーヤーのスクリーンショットです。
画像内の英語テキストを全て対応する日本語に翻訳してください。
中国語テキストがある場合はそのまま残してください。
テキスト以外の要素（背景、アイコン、レイアウト、色、UI部品の配置）は一切変更しないでください。
画像の解像度とアスペクト比も元のまま維持してください。
翻訳のみを行い、画像を再構成しないでください。"""

HARDWARE_PROMPT = """この画像はFiiO M27デジタルオーディオプレーヤーの各部名称図（ボタン・端子の説明図）です。
図中の英語ラベルテキストを全て対応する日本語に翻訳してください。
中国語テキストがある場合はそのまま残してください。
図のレイアウト、線、矢印、製品画像は一切変更しないでください。
テキストのフォントサイズと配置は元のまま維持してください。
翻訳のみを行い、画像を再構成しないでください。"""

# Image groups
GROUP_A = [
    "page6_img1.jpeg",   # Hardware diagram - uses HARDWARE_PROMPT
    "page12_img1.jpeg",
    "page13_img1.jpeg",
    "page32_img1.jpeg",
    "page32_img2.jpeg",
    "page32_img3.jpeg",
    "page33_img1.jpeg",
    "page33_img2.jpeg",
    "page33_img3.jpeg",
    "page34_img1.jpeg",
    "page34_img2.jpeg",
    "page36_img1.jpeg",
    "page36_img2.jpeg",
    "page36_img3.jpeg",
    "page36_img4.jpeg",
    "page43_img1.jpeg",
    "page43_img2.jpeg",
    "page46_img1.jpeg",
    "page51_img1.jpeg",
]

GROUP_B = [
    "page53_img1.jpeg",
    "page53_img2.jpeg",
    "page53_img3.jpeg",
    "page54_img1.jpeg",
    "page54_img2.jpeg",
    "page54_img3.jpeg",
    "page55_img1.jpeg",
    "page56_img1.jpeg",
    "page56_img2.jpeg",
    "page56_img3.jpeg",
    "page57_img1.jpeg",
    "page57_img2.jpeg",
    "page58_img1.jpeg",
    "page58_img2.jpeg",
    "page59_img1.jpeg",
    "page65_img1.jpeg",
    "page65_img2.jpeg",
    "page68_img1.jpeg",
]

ALL_IMAGES = GROUP_A + GROUP_B


def translate_image(client, filename, model=PRIMARY_MODEL, max_retries=3):
    """Translate English text in a single image to Japanese."""
    filepath = BASE_DIR / filename
    if not filepath.exists():
        print(f"  SKIP: {filename} not found")
        return False

    # Choose prompt based on image type
    prompt = HARDWARE_PROMPT if filename == "page6_img1.jpeg" else UI_PROMPT

    image = Image.open(filepath)
    original_size = image.size

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=[prompt, image],
                config=types.GenerateContentConfig(
                    response_modalities=["Text", "Image"]
                ),
            )

            # Extract generated image
            for part in response.candidates[0].content.parts:
                if part.inline_data is not None:
                    result = Image.open(BytesIO(part.inline_data.data))
                    # Save as JPEG with high quality
                    if result.mode == "RGBA":
                        result = result.convert("RGB")
                    result.save(filepath, "JPEG", quality=95)
                    new_size = result.size
                    print(f"  OK: {filename} ({original_size} -> {new_size})")
                    return True

            print(f"  WARN: {filename} - no image in response (attempt {attempt+1})")

        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                wait = 30 * (attempt + 1)
                print(f"  RATE LIMIT: {filename} - waiting {wait}s (attempt {attempt+1})")
                time.sleep(wait)
            elif "400" in error_str or "INVALID_ARGUMENT" in error_str:
                if model == PRIMARY_MODEL:
                    print(f"  FALLBACK: {filename} - trying {FALLBACK_MODEL}")
                    return translate_image(client, filename, model=FALLBACK_MODEL)
                else:
                    print(f"  FAIL: {filename} - {error_str[:100]}")
                    return False
            else:
                print(f"  ERROR: {filename} - {error_str[:100]} (attempt {attempt+1})")
                if attempt < max_retries - 1:
                    time.sleep(5)

    print(f"  FAIL: {filename} - max retries exceeded")
    return False


def main():
    # Parse arguments
    group = sys.argv[1] if len(sys.argv) > 1 else "all"

    if group == "a":
        images = GROUP_A
    elif group == "b":
        images = GROUP_B
    elif group == "all":
        images = ALL_IMAGES
    else:
        # Single image mode
        images = [group]

    print(f"=== FiiO M27 Image Translator ===")
    print(f"Group: {group} ({len(images)} images)")
    print(f"Model: {PRIMARY_MODEL}")
    print(f"Output: {BASE_DIR}")
    print()

    client = genai.Client(api_key=API_KEY)

    results = {"success": [], "failed": []}

    for i, filename in enumerate(images, 1):
        print(f"[{i}/{len(images)}] Processing {filename}...")
        success = translate_image(client, filename)
        if success:
            results["success"].append(filename)
        else:
            results["failed"].append(filename)
        # Rate limiting between requests
        if i < len(images):
            time.sleep(3)

    print()
    print(f"=== Results ===")
    print(f"Success: {len(results['success'])}/{len(images)}")
    print(f"Failed:  {len(results['failed'])}/{len(images)}")
    if results["failed"]:
        print(f"Failed files: {', '.join(results['failed'])}")

    # Write results to JSON
    results_file = BASE_DIR.parent / "translation-results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Results saved to: {results_file}")

    return 0 if not results["failed"] else 1


if __name__ == "__main__":
    sys.exit(main())
