# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

FiiO M27 取扱説明書（日本語版）の制作リポジトリ。英語PDFマニュアルを日本語レスポンシブHTMLに変換するプロジェクト。

**ソース**: `M27 Complete User manual.pdf` (3.6MB)
**出力**: `output/` 配下の3バージョンのHTML

## Python Environment

```bash
# 仮想環境の有効化
source .venv/bin/activate

# 依存パッケージ: google-genai, Pillow, PyMuPDF
pip install google-genai pillow pymupdf
```

Python 3.14、`.venv/` に仮想環境あり。

## Key Script: translate_images.py

Gemini API（`gemini-3-pro-image-preview`）を使って画像内の英語テキストを日本語に翻訳するスクリプト。

```bash
# グループ全件
python3 translate_images.py all

# グループA（19枚）またはグループB（18枚）のみ
python3 translate_images.py a
python3 translate_images.py b

# 単一ファイル
python3 translate_images.py page6_img1.jpeg
```

- API キーは `translate_images.py` の `API_KEY` 変数にハードコードされている（line 19）
- 入出力先は `output/m27-manual-ja-v3/images/` に固定
- レート制限時は自動リトライ（最大3回、30秒インターバル）
- プライマリモデルが失敗した場合、`gemini-2.5-flash-image` にフォールバック
- `page6_img1.jpeg` のみ `HARDWARE_PROMPT`（部品図用）を使用、他は `UI_PROMPT`（スクリーンショット用）

## Output Versions

| バージョン | ディレクトリ | 特徴 |
|-----------|-------------|------|
| v1 | `output/m27-manual-ja/` | 初版 |
| v2 | `output/m27-manual-ja-v2/` | レイアウト改善（Noto Sans JP、TOC、警告ボックス） |
| v3 | `output/m27-manual-ja-v3/` | 画像37枚の英語テキストを日本語化 |

v3の構成:
- `index.html` / `style.css` — v2から引き継ぎ
- `images/` — 日本語化済み画像（37枚翻訳 + 13枚オリジナル）
- `translation-results.json` — 翻訳実行ログ
- `qa-report.md` — QA検証レポート

## Skills

`/translating-pdf-manual` スキルが `~/.claude/skills/translating-pdf-manual/` にインストール済み。PDFマニュアルのHTML化・翻訳作業に使用する。スキルの仕様は以下を参照:
- `~/.claude/skills/translating-pdf-manual/HTML_SPEC.md`
- `~/.claude/skills/translating-pdf-manual/TRANSLATION_GUIDE.md`
- `~/.claude/skills/translating-pdf-manual/LAYOUT_SPEC.md`

## Translation Conventions

- 文体: です・ます体
- オーディオ用語: 業界標準のカタカナ表記
- メニューパス: `English（日本語）` 形式
- 警告ラベル: JIS Z 9101（危険 / 警告 / 注意）
