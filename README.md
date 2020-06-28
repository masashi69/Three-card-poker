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

Your Hand: ['♠4', '♠9', '♠K'] ['Flash!']

The same chips as Ante is required to match the dealer.
Do you play in your hand?: [y/n]y

===== Open Dealer Hand =====

Dealer Hand: ['♡2', '♣9', '♡4'] ["Less than Queen-high. Dealer can't play"]

You WIN!

===== Pay off =====

Pay off $30 
Pair plus bonus $50 
Ante bonus $0 

Your chips are $1050.
Continue?: [y/n]y
Your chips are $1050.
Do you want to bet ante?: [y/n]y
How much do you bet?: $10
Do you want to bet Pair plus?: [y/n]y
How much do you bet?: $10

===== Open Your Hand =====

Your Hand: ['♠7', '♣K', '♣3'] ['High card!']

The same chips as Ante is required to match the dealer.
Do you play in your hand?: [y/n]y

===== Open Dealer Hand =====

Dealer Hand: ['♠Q', '♡4', '♣5'] ['High card!']

You WIN!

===== Pay off =====

Pay off $40 
Pair plus bonus $0 
Ante bonus $0 

Your chips are $1060.
Continue?: [y/n]y
Your chips are $1060.
Do you want to bet ante?: [y/n]y
How much do you bet?: $10
Do you want to bet Pair plus?: [y/n]y
How much do you bet?: $10

===== Open Your Hand =====

Your Hand: ['♡9', '♢2', '♢3'] ['High card!']

The same chips as Ante is required to match the dealer.
Do you play in your hand?: [y/n]y

===== Open Dealer Hand =====

Dealer Hand: ['♢10', '♣2', '♢7'] ["Less than Queen-high. Dealer can't play"]

You WIN!

===== Pay off =====

Pay off $30 
Pair plus bonus $0 
Ante bonus $0 

Your chips are $1060.
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
The simulator trials 100 times.
You\'ll bet ante $10 and pair plus $10 all the time.

=== Probabliry of winning or losing ===

Player 54 wins. (54.0%)
Dealer 46 wins. (46.0%)
Draw 0 times. (0.0%)

=== Percentage of Players all hands ===

High card!            75.0%
One Pair!             12.0%
Flash!                 7.0%
Straight!              6.0%

=== Percentage of Players win(54 times) hands ===

High card!          61.111%
One Pair!           16.667%
Flash!              11.111%
Straight!           11.111%

You finally got $-470
```
