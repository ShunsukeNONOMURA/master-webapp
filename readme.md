# webapp fastapi master
python(fastapi)によるwebアプリ開発用のマスタ。  
[mkdocs](https://shunsukenonomura.github.io/webapp-fastapi-master/mkdocs/index.html)でドキュメンテーション実施。

## TODO
- 排他制御
    - https://sqlalchemy.narkive.com/RbfOgJvz/how-to-use-version-id-col
    - https://weseek.co.jp/tech/525/
    - https://qiita.com/tatsurou313/items/053cffdfe940a89d7f5a
- 共通型
    - enum
- エラーハンドリング＋ロギング
    - エラーモデル
    - API
- ドキュメンテーション
    - sphinx
- CI
    - github action
- Auth
    - keycloak連携
        - https://fastapi-keycloak-middleware.readthedocs.io/en/latest/usage.html
        - https://qiita.com/KWS_0901/items/bdf60a725064900eaad1

```
python db.py
sqlite3 dev.sqlite3
sqlite_web dev.sqlite3
```

## 開発フロー
- 要求解析
- モデリング
    - **情報設計 / 集約設計**
    - ORM設計開発
        - ドキュメント生成：ER図
    - ドメインモデル実装
- アプリ開発（ドメイン毎等）
    - IF設計開発
        - ドキュメント生成：API仕様書
    - （テスト駆動：スタブ実装 / APIテスト実装）
    - サービス実装
    - ユースケース実装
    - モジュール結合
    - APIテスト実行
        - ドキュメント生成：テストカバレッジ
- 結合評価
- リリース
