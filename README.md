# Three-card-poker
スリーカードポーカーゲーム

## ルール

* デッキはジョーカー無しの52枚
* 3枚のカードでポーカーを行う
* 勝負はディーラーと1対1
* 手札の交換はできない
* ディーラーはQハイカード以上でないと勝負できない

## 役

降順で強い

* ストレートフラッシュ
* スリーオブアカインド
* ストレート
* フラッシュ
* ワンペア
* ハイカード

## サンプル

```ｓh
$ python3 pokerapp.py 
Player Hand: ['S3', 'C12', 'C5'] ['High card!']
Dealer Hand: ['H3', 'S9', 'S4'] ["Dealer can't play"]

Player WIN!
$ python3 pokerapp.py 
Player Hand: ['D10', 'C8', 'D7'] ['High card!']
Dealer Hand: ['D2', 'D14', 'H4'] ['High card!']

Dealer WIN!
$ python3 pokerapp.py 
Player Hand: ['S2', 'S8', 'S3'] ['Flash!']
Dealer Hand: ['S6', 'C10', 'H12'] ['High card!']

Player WIN!
```

## 追加したい機能


* 手札の清書
  - スートを記号(♠,♥,♦,♣)に変換する
  - エース、絵柄を文字(A,K,Q,J)に変換する
* チップの処理追加
  - アンティ(場代)
  - ペアプラス
  - ベット or フォールド
  - 払い戻し
* シミュレータの作成
* テストコード作成
* GUI化
