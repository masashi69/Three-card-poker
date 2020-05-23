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
Player Hand: ['♡5', '♢K', '♡6'] ['High card!']
Dealer Hand: ['♢9', '♢J', '♢Q'] ['Flash!']

Dealer WIN!
$ python3 pokerapp.py 
Player Hand: ['♢9', '♢J', '♣2'] ['High card!']
Dealer Hand: ['♢10', '♠K', '♣K'] ['One Pair!']

Dealer WIN!
$ python3 pokerapp.py 
Player Hand: ['♣A', '♡6', '♡J'] ['High card!']
Dealer Hand: ['♠2', '♣5', '♠3'] ["Less than Queen-high. Dealer can't play"]

Player WIN!
```

## 追加したい機能

* チップの処理追加
  - アンティ(場代)
  - ペアプラス
  - ベット or フォールド
  - 払い戻し
* シミュレータの作成
* テストコード作成
* GUI化
