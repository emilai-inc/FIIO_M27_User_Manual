# FiiO M27 取扱説明書（日本語版）

FiiO M27 Complete User Manual の日本語HTMLマニュアルです。

英語PDFマニュアルを日本語に翻訳し、レスポンシブHTMLとして構築しています。

## バージョン一覧

| バージョン | 内容 | GitHub Pages |
|-----------|------|-------------|
| v1 (m27-manual-ja) | 初版：PDFからの日本語翻訳 | [v1を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja/) |
| v2 (m27-manual-ja-v2) | レイアウト改善：画像サイズ適正化、Noto Sans JP、セクション番号、TOC改善 | [v2を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja-v2/) |
| v3 (m27-manual-ja-v3) | 画像日本語化：Nano Banana ProでUIスクショ37枚の英語テキストを日本語に翻訳 | [v3を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja-v3/) |

## ファイル構成

```
output/
├── m27-manual-ja/           # v1: 初版
├── m27-manual-ja-v2/        # v2: レイアウト改善版
│   ├── index.html           # 改善済みHTML（figureクラス分類、Google Fonts等）
│   ├── style.css            # モダンCSS（665行）
│   ├── images/              # オリジナル画像（50枚）
│   └── ...
├── m27-manual-ja-v3/        # v3: 画像日本語化版
│   ├── index.html           # v2と同一HTML
│   ├── style.css            # v2と同一CSS
│   ├── images/              # 日本語化済み画像（37枚翻訳 + 13枚オリジナル）
│   ├── translation-results.json  # 翻訳結果ログ
│   └── ...
└── translate_images.py      # Gemini API画像翻訳スクリプト
```

## 各バージョンの改善内容

### v1 → v2 の変更点
- 画像サイズ適正化（スマホUI: 360px、部品図: 620px、カバー: 480px）
- Google Fonts（Noto Sans JP + Inter）
- CSSカウンターによるセクション番号自動付与
- TOCをカード風2カラムレイアウトに
- 警告ボックスにアイコン追加（⛔ 危険 / ⚠️ 警告 / ℹ️ 注意）
- テーブルのモダン化（角丸、ホバーエフェクト）
- 「トップに戻る」ボタン追加
- 768pxブレークポイント追加

### v2 → v3 の変更点
- Nano Banana Pro（Gemini 3 Pro Image）APIでUIスクリーンショット37枚の英語テキストを日本語化
- システム設定画面（Settings, Audio, Display, Bluetooth等）19枚
- FiiO Musicアプリ画面（ホーム、再生、EQ等）15枚
- ファームウェア・デバイス情報画面 3枚
- ハードウェア部品図（各部名称ラベル）1枚

## 内容

- 外観ガイド（ボタン・端子の説明）
- 製品概要・クイックスタート
- 6つの動作モード（Android / Pure Music / AirPlay / USB DAC / Bluetooth受信 / 同軸）
- デスクトップモード・Bluetoothトランスミッター
- よく使う機能（スクリーンショット / FiiO Link / DLNA / Roon Ready / 光・同軸出力）
- システム設定・FiiO Music・テープモード
- 仕様・FAQ・安全情報

## 翻訳仕様

- です・ます体
- オーディオ専門用語は業界標準のカタカナ表記に準拠
- メニューパスは `English（日本語）` 形式
- 警告ラベルはJIS Z 9101に準拠（危険 / 警告 / 注意）

## 技術スタック

- **翻訳**: Claude Code (Agent Teams)
- **画像日本語化**: Google Gemini Nano Banana Pro (gemini-3-pro-image-preview)
- **画像抽出**: PyMuPDF (pymupdf)
- **QA**: 自動化検証スクリプト
