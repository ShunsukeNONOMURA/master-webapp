# ORM設計

## 全般
- [SQLModel](https://sqlmodel.tiangolo.com/)を利用
    - FastAPIと同じ作者のsqlalchemyとpydanticのラッパー
- 必要に応じて基底クラスを作る
    - プレフィックス毎の性質共通化ぐらいまで
- SQLModelの基本的な記述だけだと困る場合、schemaspy記述も併用する
- [アプリで利用するリレーションは正しく貼る](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/define-relationships-attributes/#define-relationships-attributes)
    - 単数か複数かは正しく記述すること
    - 外部キーやback_populates等のオプション記述も必要に応じて正しく記述する
- ドキュメントリバース対応としてコメントは入れる。コメントで書ききれないものは別途記述する。
- 「ヒストリテーブル」と「通常のトランザクションテーブル/マスタテーブル」の間に外部制約を入れない
- ER図生成による可視化はschemaspyなどを用いてマイグレーション後のDDLからリバースする
- どのように型変換されるかは理解しておくこと
    - [参考：【SQLAlchemy】Generic Typesと各種DBの型 対応表](https://zenn.dev/re24_1986/articles/8520ac3f9a0187)

## 命名規則
- クラス名
    - クラス名PEP8に倣い、CapWords方式で記載する。
    - プレフィックスは正しく振ること
- テーブル名
    - テーブル名はRDB側はケース・インセンシティブなのでsnake_caseとする。
    - プレフィックスは正しく振ること
- プロパティ
    - 予約プロパティは必要に応じて組み込む
    - それ以外のプロパティはシンプルな記述を心がける

## テーブル名(クラス名)プレフィックス
| 文字 | 意味             |
| ---- | ---------------- |
| m    | マスタ           |
| t    | トランザクション |
| h    | ヒストリ         |

## 予約プロパティ
| プロパティ | Python型ヒント | sqlmodel.Field の参考                              | 役割                 |
| ---------- | -------------- | -------------------------------------------------- | -------------------- |
| code       | str            | Field(max_length = 2, nullable=False, unique=True) | 意味のある記号列採番 |
| created_at | datetime       |                                                    | 作成日               |
| updated_at | datetime       |                                                    | 更新日、楽観的ロック |

<!-- ## 予約プロパティ



## バグ
- oracleだとschemaspyでukにfk制約かけると表示されないバグ
    - 制約自体は晴れている
    - 同じ不具合出ている人がいる
        - https://github.com/schemaspy/schemaspy/issues/1430
    - 止まってられないので、一旦postgresqlで進める。 -->


## 検討中：ドメインモデル
- プロパティ名はモデル名を含める
    - user_name
    - group_name
- 汎用プロパティは共通名
    - created_at
    - updated_at