# はじめに
FastAPIのベースラインリポジトリに関するドキュメント

## Links
- https://github.com/ShunsukeNONOMURA/master-webapp
- https://shunsukenonomura.github.io/master-webapp/backend/api.html
- https://shunsukenonomura.github.io/master-webapp/backend/oss.html
- https://shunsukenonomura.github.io/master-webapp/backend/pytest_cov/index.html
- https://shunsukenonomura.github.io/master-webapp/rdb/schemaspy/index.html

## 参考
- https://shunsukenonomura.github.io/mkdocs-development/volume/site/0300-design-api.html
- https://shunsukenonomura.github.io/mkdocs-development/volume/site/0350-design-ddd-cqrs.html
- https://shunsukenonomura.github.io/mkdocs-development/volume/site/0400-example-ddd.html

## TODO
- Entityがidが等しければ同じものであることをどのように周知するか
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
    - (mkdocs)
- conflict
    - sqlmodel, id
- CI
    - github action
- Auth
    - keycloak連携
        - https://fastapi-keycloak-middleware.readthedocs.io/en/latest/usage.html
        - https://qiita.com/KWS_0901/items/bdf60a725064900eaad1

