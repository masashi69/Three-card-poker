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

## 払い戻し

* ディーラー勝負
  - アンティ 1:1
  - プレイヤーベット 1:1

* ペアプラスボーナス
  - ストレートフラッシュ 40:1
  - スリーオブアカインド 30:1
  - ストレート 6:1
  - フラッシュ 4:1
  - ワンペア 1:1

* アンティボーナス
  - ストレートフラッシュ 5:1
  - スリーオブアカインド 4:1
  - ストレート 1:1


## サンプル

```ｓh
$ python3 pokerapp.py 
Your chips are 1000
Do you want to bet ante?: [y/n]y
How much do you bet?: 100
Do you want to bet Pair plus?: [y/n]y
How much do you bet?: 100

===== Open Your Hand =====

Your Hand: ['♡4', '♣Q', '♡A'] ['High card!']

The same chips as Ante is required to match the dealer.
Do you play in your hand?: [y/n]y

===== Open Dealer Hand =====

Dealer Hand: ['♢5', '♣J', '♡3'] ["Less than Queen-high. Dealer can't play"]

You WIN!
Your chips are 1400
Continue?: [y/n]y
Your chips are 1400
Do you want to bet ante?: [y/n]y
How much do you bet?: 100
Do you want to bet Pair plus?: [y/n]y
How much do you bet?: 100

===== Open Your Hand =====

Your Hand: ['♠10', '♡7', '♣7'] ['One Pair!']

The same chips as Ante is required to match the dealer.
Do you play in your hand?: [y/n]y

===== Open Dealer Hand =====

Dealer Hand: ['♣Q', '♠A', '♢7'] ['High card!']

You WIN!
Your chips are 1900
Continue?: [y/n]
```

## 追加したい機能

* シミュレータの作成
* テストコード作成
* GUI化
