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

```sh
$ python3 pokerapp.py 
Your chips are $1000.
Do you want to bet ante?: [y/n]y
How much do you bet?: $10
Do you want to bet Pair plus?: [y/n]y
How much do you bet?: $10

===== Open Your Hand =====

Your Hand: ['♠9', '♠K', '♠4'] ['Flash!']

The same chips as Ante is required to match the dealer.
Do you play in your hand?: [y/n]y

===== Open Dealer Hand =====

Dealer Hand: ['♣Q', '♡8', '♠6'] ['High card!']

You WIN!

===== Pay off =====

Pay off $40 
Pair plus bonus $40 
Ante bonus $0 

Your chips are $1080.
Continue?: [y/n]y
Your chips are $1080.
Do you want to bet ante?: [y/n]y
How much do you bet?: $100
Do you want to bet Pair plus?: [y/n]y
How much do you bet?: $100

===== Open Your Hand =====

Your Hand: ['♣J', '♡8', '♠7'] ['High card!']

The same chips as Ante is required to match the dealer.
Do you play in your hand?: [y/n]y

===== Open Dealer Hand =====

Dealer Hand: ['♢10', '♣A', '♠9'] ['High card!']

Dealer WIN!

===== Pay off =====

Pay off $0 
Pair plus bonus $0 
Ante bonus $0 

Your chips are $780.
Continue?: [y/n]
```

## 追加したい機能

* GUI化

## シミュレータ

* 勝負を50万回施行
* 勝率、役の分布を出力

```sh
$ python3 simulater.py 
Three card poker simulator start.
The simulator trials 500000 times.

=== Probabliry of winning or losing ===

Dealer 249544 wins.
Player 250456 wins.

=== Percentage of Players hands ===

High card!          74.667%
One Pair!           16.956%
Flash!               4.975%
Straight!            2.977%
Three of a kind!     0.241%
Straight Flash!      0.184%
```