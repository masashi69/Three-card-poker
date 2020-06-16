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

* 勝負をtrialの回数施行
* 勝率、役の分布を出力
* アンティ、ペアプラスの賭け金をシミュレート
  - プレイヤーはfoldしない

```sh
$ python3 simulater.py 
You are first given $1,000.
Three card poker simulator start.
The simulator trials 500,000 times.
You\'ll bet ante $10 and pair plus $10 all the time.

=== Probabliry of winning or losing ===

Player 271219 wins. (54.2%)
Dealer 228442 wins. (45.7%)
Draw 339 times. (0.1%)

=== Percentage of Players all hands ===

High card!          74.717%
One Pair!           16.891%
Flash!                4.99%
Straight!            2.967%
Three of a kind!     0.236%
Straight Flash!        0.2%

=== Percentage of Players win(271,219 times) hands ===

High card!          59.334%
One Pair!           25.857%
Flash!                8.66%
Straight!            5.348%
Three of a kind!     0.434%
Straight Flash!      0.368%

You finally got $7469850
```
