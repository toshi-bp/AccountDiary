# AccountDiary
## 概要
家計簿と思い出を一緒に記録するサービス

## ターゲット層
- インスタグラムを利用していて、家計簿を使っていない人

## 使用技術
- フロントエンド
    - vue.js(javascript)
- サーバーサイド
    - flask(python)
- データベース
    - sqlite
- ホスティング
    - google app engine(予定)

## ユーザーストーリーリスト
| 内容 | ポイント(大きい方優先) |
| --- | --- |
| 収支の入力→完了 | 10 |
| 写真のアップロード機能→完了 | 9.5 |
| 写真をタップするとどれだけ使ったかを表示する機能→完了 | 9 |
| カテゴリの用意(初期は少なめ)→完了| 8.5 |
| パスワード機能→完了 | 8 |
| グラフ表示機能→多分　完了 | 7.5 |
| レシート読み取り機能 | 4.5 |
| 今月使うお金の設定→予算の設定はできるようにした | 6 |
| アラート機能（通知ではなくページ上） | 5.5 |
| 自分で勝手に決める、提案機能 | 5 |
| お金の単位、100円以下切り捨て →完了| 4.5 |
| #で検索機能、タグ分け（ホーム画面）| 4 |
| 思い出に点数付け（提案、ランキング化に使用）→完了| 3.5 |

## リポジトリ構成

## データベースの構造
### テーブル名
| カラム名 | データ型 | 主キーか |
| --- | --- | --- |
||||

### users
| カラム名 | データ型 | 備考 |
| --- | --- | --- |
| id | TEXT | 主キー |
| mail | TEXT | メアド |
| pwd | TEXT | パスワード |
| name | TEXT | ユーザーネーム |
| birthday | TEXT | 生年月日 |
| gender | TEXT | 性別 |
| phonenumber | TEXT | 電話番号 |
| money | INTEGER | 所持金(初期値は0) |
| used_money | INTEGER | (使ったお金, 初期値は0) |
| jti | TEXT | アクセストークン(認証の際に使用) |

### images(インスタ的な部分)
| カラム名 | データ型 | 備考 |
| --- | --- | --- |
| id | INTEGER | 主キー |
| user_id | TEXT | usersのidと照会 |
| image_url | TEXT | 画像URL |
| file_name | TEXT | アップロードされる画像のファイル名 |
| act_time | TEXT | 初回投稿の際の日付orその行動を行なった日付 |
| update_time | TEXT | 更新した際の日付 |
| diary | TEXT | 日記の文章 |
| score | INTEGER | その思い出の点数 |
| cost | INTEGER | 払ったお金 |

### histories(行動履歴)
| カラム名 | データ型 | 備考 |
| --- | --- | --- |
| id | INTEGER | 主キー |
| user_id | INTEGER | membershipのidと照会 |
| action | TEXT |  |
| result | INTEGER | 行動の結果による収入or支出 |
| act_time | TEXT | 初回投稿の際の日付orその行動を行なった日付 |
| update_time | TEXT | 更新した際の日付 |
| type | TEXT | 収入or支出 |
| category | TEXT | カテゴリ(categoriesと照会) |
| place | TEXT | 場所 |

### categories(カテゴリー一覧)
| カラム名 | データ型 | 備考 |
| --- | --- | --- |
| id | INTEGER | 主キー |
| user_id | TEXT | ユーザー毎のカテゴリー一覧を表示する際に利用 |
| type | TEXT | 収入or支出 |
| category | TEXT | カテゴリー |



## 必要となる画面
1. ログイン画面
1. 会員登録画面
1. 家計簿の記録をまとめた画面
    - グラフ
    - 金額の表示
1. アップロードされた画像を表示する画面

## 中間発表フィードバック
- 家計簿が続かない人のデータなくね？
- カテゴリに応じたアラート機能あるといいよね
- paypayとの連携, 位置情報連携
- 家計簿は収支の抜け漏れが出ること
- ターゲット層を絞る？？
- サブスクの金を記録しておいて,
- 遊びに使うお金に絞る??

## 改善点(今後作成を続ける際に...)
- レスポンシブ対応
- ユーザー名の被りを防止する
- 会員登録の際に認証メールを送信できるようにする
- 電話番号及びメアドの形の制限(正規表現を利用)
- アバター機能
- paypayなどの外部サービスとの連携
- コンポーネントの分割(リファクタリング)
- 入力データの型判定(typeof関数を利用)