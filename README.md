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
masashi@PC-ubuntu:~/Three-card-poker$ python3 simulater.py 
You are first given $1,000.
Three card poker simulator start.
The simulator trials 1,000 times.
You\'ll bet ante $10 and pair plus $10 all the time.

You could play the game 301 times.

=== Probabliry of winning or losing ===

Player 156 wins. (51.8%)
Dealer 144 wins. (47.8%)
Draw 1 times. (0.3%)

=== Percentage of Players all hands ===

High card!          74.751%
One Pair!           18.605%
Flash!               4.319%
Straight!            1.993%
Straight Flash!      0.332%

=== Percentage of Players win(156 times) hands ===

High card!          59.615%
One Pair!           27.564%
Flash!               8.333%
Straight!            3.846%
Straight Flash!      0.641%

You finally got $10
```
