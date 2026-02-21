# FiiO M27 取扱説明書（日本語版）

FiiO M27 Complete User Manual の日本語HTMLマニュアルです。

英語PDFマニュアルを日本語に翻訳し、レスポンシブHTMLとして構築しています。

## バージョン一覧

| バージョン | 内容 | GitHub Pages |
|-----------|------|-------------|
| v1 (m27-manual-ja) | 初版：PDFからの日本語翻訳 | [v1を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja/) |
| v2 (m27-manual-ja-v2) | レイアウト改善：画像サイズ適正化、Noto Sans JP、セクション番号、TOC改善 | [v2を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja-v2/) |
| v3 (m27-manual-ja-v3) | 画像日本語化：Nano Banana ProでUIスクショ37枚の英語テキストを日本語に翻訳 | [v3を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja-v3/) |
| v4 (m27-manual-ja-v4) | デュアルQAレビュー改善：Claude + Geminiによる翻訳精度向上・コード品質改善 | [v4を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja-v4/) |
| v5 (m27-manual-ja-v5) | PDF原文全ページ対照：Audio/Display/Global設定完全版+FAQ15項目追加+細部修正16箇所 | [v5を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja-v5/) |
| v6 (m27-manual-ja-v6) | Gemini 3.1 Pro再検証：誤訳修正・訳抜け補完・アクセシビリティ改善（95点/100点） | [v6を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja-v6/) |
| v7 (m27-manual-ja-v7) | 全18セクション×1対1全文対比チェック：真の訳抜け3件修正・誤訳0件確認（最終版） | [v7を表示](https://kenzokono.github.io/FIIO_M27_User_Manual/output/m27-manual-ja-v7/) |

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
├── m27-manual-ja-v4/        # v4: デュアルQAレビュー改善版
│   ├── index.html           # 翻訳・コード改善済みHTML
│   ├── style.css            # 改善済みCSS
│   ├── images/              # v3と同一（日本語化済み画像）
│   ├── qa-report.md         # v4用デュアルQAレポート
│   └── ...
├── m27-manual-ja-v5/        # v5: PDF全ページ対照・完全版
│   ├── index.html           # 全セクション拡充済みHTML（1881行）
│   ├── style.css            # v4と同一CSS
│   ├── images/              # v3と同一（日本語化済み画像）
│   ├── qa-report.md         # v5用PDF対照QAレポート
│   └── ...
├── m27-manual-ja-v6/        # v6: Gemini 3.1 Pro再検証版
│   ├── index.html           # 最終改善版HTML（1924行）
│   ├── style.css            # v6 CSS
│   ├── images/              # v3と同一（日本語化済み画像）
│   ├── qa-report.md         # v6用Gemini 3.1 ProQAレポート
│   └── ...
├── m27-manual-ja-v7/        # v7: 全文対比検証済み最終版
│   ├── index.html           # 全文対比済みHTML
│   ├── style.css            # v7 CSS
│   ├── images/              # v3と同一（日本語化済み画像）
│   ├── qa-report.md         # v7用全文対比QAレポート
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
- Gemini 3 Pro Image Preview（Nano Banana Pro）APIでUIスクリーンショット37枚の英語テキストを日本語化
- システム設定画面（Settings, Audio, Display, Bluetooth等）19枚
- FiiO Musicアプリ画面（ホーム、再生、EQ等）15枚
- ファームウェア・デバイス情報画面 3枚
- ハードウェア部品図（各部名称ラベル）1枚

### v3 → v4 の変更点
- デュアルQA（Claude + Gemini 2.5 Flash）によるクロスレビュー実施
- 翻訳精度向上：「搭載」重複修正、FiiO Link括弧書きの自然化、ファクトリーリストアモード表現改善
- 用語統一：S/PDIF表記の統一（FAQ内の不要な括弧削除）
- 自然な日本語：Wi-Fiスリープ設定の助詞改善、読点追加
- HTML構造：TOCに `#usb-digital-output` リンク追加、余分な空行削除
- CSSバージョンコメント更新

### v4 → v5 の変更点
- **PDF原文68ページとの全セクション逐一対照**（Gemini 2.5 Flash で5チャンク検証）
- Audio設定: 6項目→17項目（Bluetoothコーデック、LDAC/LHDC品質、音量調整、3.5mm/4.4mm出力モード切替、SPDIF OUT、PEQ、第2次高調波、自動一時停止等）
- Display設定: 4項目→10項目（明るさ、LEDライト制御、ナイトライト、表示サイズ、ロック画面、自動回転）
- Global設定: 2項目→7項目（マルチファンクションボタン、電源オフタイマー、HOLDスイッチ、音量設定、ダブルタップ復帰）
- FAQ: 7項目→22項目（USB DACスマホ接続、AirPlay、Roon Ready、FiiO Cast、DK1 PLUS、スーパーハイゲイン等15項目追加）
- ゲイン設定修正: 3段階→5段階（PDF準拠）
- 出力端子仕様修正: 同時出力不可→同時出力可能（PDF準拠）
- 各セクション細部: 外観ガイド6箇所、FiiO Link手順、ファームウェア注記等16箇所修正

### v5 → v6 の変更点
- **Gemini 3.1 Pro Preview による全面再検証**（PDF 3チャンク対照 + 品質レビュー、95点/100点）
- 誤訳修正: USB Type-C（データ）充電対応、6.35mmライン出力追加、強制再起動条件修正
- 訳抜け補完: 出力優先順位、BT受信ペアリング手順、DLNA制限注記、FW所要時間、invalid imageトラブルシューティング、アンテナ注意、デスクトップモードバッテリー注記
- 翻訳品質: メニューパス形式7箇所統一、40文字超長文4箇所分割、2次高調波の表現正確化
- アクセシビリティ: CSPメタタグ追加、nav aria-label追加
- スペック値注記: PDF内の値の不一致について注意書き追加

### v6 → v7 の変更点
- **全18セクション × 1対1 PDF原文対照**（Gemini 3.1 Pro で各セクション個別検証）
- 誤検知フィルタリング: PDF（FAQ形式）とHTML（マニュアル形式）の構造差異を考慮し、真の問題のみ抽出
- 真の訳抜け3件修正: 電源オフ時の再起動選択肢、microSD読み書き速度、初回起動時の言語選択
- 真の誤訳: **0件確認**（翻訳は正確）
- ゲインモード別出力値（Super High: 2250mW、Ultra High: 5000mW）を仕様注記に追記

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
- **画像日本語化**: Gemini 3 Pro Image Preview / Nano Banana Pro (gemini-3-pro-image-preview)、フォールバック: Nano Banana (gemini-2.5-flash-image)
- **画像抽出**: PyMuPDF (pymupdf)
- **QA (v4)**: デュアルQA — Claude Opus 4.6 + Gemini 2.5 Flash
- **QA (v5)**: PDF原文対照 — Gemini 2.5 Flash（5チャンク逐一検証）
- **QA (v6)**: 全面再検証 — Gemini 3.1 Pro Preview（3チャンク対照 + 品質レビュー）
- **QA (v7)**: 全文対比 — Gemini 3.1 Pro Preview（18セクション×1対1対照 + 誤検知フィルタリング）
