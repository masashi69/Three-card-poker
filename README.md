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
$ python3 pockerapp.py Player Hand: ['S3', 'C12', 'C5'] ['High card!']
Dealer Hand: ['H3', 'S9', 'S4'] ["Dealer can't play"]

Player WIN!
$ python3 pockerapp.py Player Hand: ['D10', 'C8', 'D7'] ['High card!']
Dealer Hand: ['D2', 'D14', 'H4'] ['High card!']

Dealer WIN!
$ python3 pockerapp.py Player Hand: ['S2', 'S8', 'S3'] ['Flash!']
Dealer Hand: ['S6', 'C10', 'H12'] ['High card!']

Player WIN!
```

