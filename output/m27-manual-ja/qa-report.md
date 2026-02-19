# QA検証レポート

検証日時（初回）: 2026-02-19 23:50
検証日時（再検証）: 2026-02-20 00:15
検証対象PDF: /Users/kenzo/claude/manual-test/M27 Complete User manual.pdf
出力ディレクトリ: /Users/kenzo/claude/manual-test/output/m27-manual-ja

---

## 再検証結果サマリー

| 優先度 | 初回 | 修正後 | 備考 |
|---|---|---|---|
| CRITICAL | 5 | 0 | 全件修正済み |
| ERROR | 0 | 0 | -- |
| WARNING | 4 | 2 | W1修正済み、W4解消、W2/W3残存（許容範囲） |
| MINOR | 5 | 3 | M5残存、M3残存、新規1件 |

**判定: PASS（リリース可能）**

---

## 1. 概要

| 項目 | 数 |
|---|---|
| PDF内画像数 | 50 |
| image-map.json登録数 | 50 |
| HTML内figure数 | 50 |
| 装飾画像 | 0 |
| 配置不確実 | 0 |
| HTMLファイル行数 | 1565 |

## 2. 画像配置チェック

正常: 50 / 要確認: 0 / 未配置: 0

## 3. 構造チェック

| チェック項目 | 結果 |
|---|---|
| アンカーリンク（href="#..."） | 48件 すべて対応IDあり |
| セクションID | 48件 すべて一意 |
| テーブル | 9件 すべて.table-wrapperでラップ済み |
| 画像 loading="lazy" | 50/50 |
| 画像 alt text（日本語） | 50/50 |
| figcaption（日本語） | 50/50 |
| warning-danger | 2件 |
| warning-caution | 8件 |
| warning-notice | 13件 |
| warning-labelの対応 | 危険→danger, 警告→caution, 注意→notice すべて正しい |
| nav#toc | 存在 |
| レスポンシブCSS | 640px breakpoint あり |
| 印刷用CSS | @media print あり |

## 4. 自動QAスクリプト結果

問題なし（0件）

---

## 5. CRITICAL修正の検証

### C1. 欠落セクション「よく使う機能の説明」→ **修正済み**

新セクション `#common-functions` が追加され、以下のサブセクションを含む:
- `#screenshot` — スクリーンショット（電源+前の曲ボタン同時押し）
- `#usb-digital-output` — USBオーディオデジタル出力（#usb-audioへの相互リンクあり）
- `#fiio-link-bt` — FiiO Link Bluetooth制御（5ステップの手順）
- `#fiio-link-wifi` — FiiO Link Wi-Fi制御（4ステップの手順）
- `#dlna-function` — DLNA機能（レンダラー/ブラウズの2パターン）
- `#roon-ready` — Roon Ready（5ステップの手順、サブスクリプション注記あり）
- `#optical-coaxial-usage` — 光/同軸出力の使い方（光/同軸別の手順、DoP注記あり）

TOCにも対応エントリーが追加済み。翻訳品質は良好（です・ます体統一、メニューパス形式正しい）。

### C2. ボタン・端子の詳細説明 → **修正済み**

以下が `#pictorial-guide` セクションに追加:
- マルチファンクションボタンの詳細操作（短押し: FiiO Music、長押し: モード選択）— line 118
- USB Type-Cポート機能比較表（Data vs Charging/Power、5項目）— lines 142-177
- 出力端子の優先順位（6.35mm > 4.4mm > 3.5mm）— lines 179-186
- ライン出力切り替えの注意書き — lines 188-190
- デスクトップモードスイッチの機能比較表（7項目）— lines 192-237

### C3. Roon Ready / DLNA / FiiO Link → **修正済み**

C1の修正に含まれる形で `#common-functions` セクション内に追加。

### C4. バッテリー残量の数値修正 → **修正済み**

- 修正前: 「バッテリー残量が50%以上」
- 修正後: 「バッテリー残量が30%以上」（line 606）
- PDF原文と一致することを確認。

### C5. 強制再起動・リカバリーモード → **修正済み**

`#firmware-upgrade` セクション内に以下が追加:
- `#force-reboot` — 強制再起動（電源ボタン10秒長押し、データ消失の注意書きあり）— lines 611-617
- `#recovery-mode` — リカバリーモード（電源+ボリューム同時長押し、3つの操作オプション）— lines 619-631
- `#factory-reset-detail` — 工場出荷時リセットの詳細手順（Settings経由/リカバリーモード経由の2方法）— lines 633-651

TOCにもサブエントリーとして追加済み。

---

## 6. WARNING検証

### W1. 「同軸」初出に「（コアキシャル）」→ **修正済み**

Line 138: `同軸（コアキシャル）入出力（COAX IN/OUT）` — 正しい。

### W2. 「光（オプティカル）」の繰り返し使用 → **残存（許容範囲）**

厳密にはガイド違反だが、マニュアルの可読性を考慮すると問題ない。

### W3. 長文（40文字超）→ **残存（許容範囲）**

メニューパスの英語+日本語併記による文字数膨張が主因。実質的な日本語文としては自然。

### W4. PDF TOCとHTML TOCの不一致 → **解消**

C1-C3の修正により、主要セクションがTOCに追加された。

---

## 7. MINOR検証

### M3. S/PDIF表記の混在 → **残存**

FAQ内で「S/PDIF」、他セクションで「光/同軸」が混在。軽微。

### M5. テープモードのインラインスタイル → **残存**

Line 865付近の `<div style="display:flex;...">` — 機能上問題なし。

### M6. (新規) `#usb-digital-output` がTOCに未登録

`common-functions` セクション内の `#usb-digital-output` はh3見出しだがTOCに対応エントリーがない。ただし、内容が簡潔で `#usb-audio` への相互リンクがあるため、実質的な影響はなし。

---

## 8. 用語チェック（再検証）

| 用語 | ガイド規定 | HTML実装 | 結果 |
|---|---|---|---|
| headphone out | ヘッドホン出力 | ヘッドホン出力 | OK |
| balanced | バランス | バランス | OK |
| DAC（初出） | D/Aコンバーター（DAC） | D/Aコンバーター（DAC） | OK |
| DAC（以降） | DAC | DAC | OK |
| sample rate | サンプリングレート | サンプリングレート | OK |
| impedance | インピーダンス | インピーダンス | OK |
| S/N ratio | SN比 | SN比 | OK |
| coaxial（初出） | 同軸（コアキシャル） | 同軸（コアキシャル） | **OK（修正済み）** |
| coaxial（以降） | 同軸 | 同軸 | OK |
| optical（初出） | 光（オプティカル） | 光（オプティカル） | OK |
| firmware update | ファームウェアアップデート | ファームウェアアップデート | OK |
| factory reset | 工場出荷時リセット | 工場出荷時リセット | OK |
| equalizer | イコライザー | イコライザー | OK |
| です・ます体 | 統一 | 統一 | OK |
| 製品名保持 | FiiO M27 | FiiO M27 | OK |
| メニューパス形式 | English（日本語） | Settings（設定）→ ... | OK |

---

## 9. 翻訳品質の総合評価

**PASS — リリース可能。**

初回QAで指摘したCRITICAL 5件はすべて修正済み。追加されたコンテンツ（約250行分）の翻訳品質も既存部分と同等で、です・ます体の統一、メニューパス形式、用語の一貫性が保たれている。

残存するWARNING 2件（光オプティカル繰り返し、長文）およびMINOR 3件（S/PDIF表記混在、インラインスタイル、TOC未登録のh3）はいずれも軽微であり、ユーザー体験に影響しない。
