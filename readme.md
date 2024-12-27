# master webapp
python(fastapi)によるwebアプリ開発用のマスタ。

## Links
- https://shunsukenonomura.github.io/master-webapp/mkdocs/index.html
    - mkdocsの外部サイト

## backend構成
| パス                          | 役割                                      |
| ----------------------------- | ----------------------------------------- |
| app/core                      | 共通で利用するモジュールなどを配置        |
| app/core/abstract             | 共通で利用する抽象クラス                  |
| app/core/exception            | 共通で利用するException                   |
| app/core/middleware           | 共通で利用するミドルウェア                |
| app/ddd                       | DDDを表現する                             |
| app/ddd/presentation          | DDD：プレゼンテーション層                 |
| app/ddd/presentation/schema   | DDD：プレゼンテーション層の入出力スキーマ |
| app/ddd/presentation/endpoint | DDD：プレゼンテーション層のエンドポイント |
| app/ddd/application           | DDD：ユースケース層                       |
| app/ddd/application/schema    | DDD：ユースケース層の入出力スキーマ       |
| app/ddd/application/usecase   | DDD：ユースケース層のユースケース         |
| app/ddd/domain                | DDD：ドメイン層                           |
| app/ddd/infra                 | DDD：インフラ層                           |
| app/ddd/infra/database        | DDD：インフラ層のデータベース実装         |
| app/ddd/infra/repository      | DDD：インフラ層のリポジトリ実装           |
| app/ddd/infra/router          | DDD：インフラ層のルーティング実装         |
| app/main.py                   | 起動ファイル                              |
| migrations                    | ORMやマイグレーション                     |
| migrations/model              | ORM                                       |
| tests                         | test関連                                  |
| pyproject.toml                | poetry設定                                |

## コマンドシート
| 操作                                     | コマンド                                                                                                                                                          |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| コンテナ起動                             | `docker compose up`                                                                                                                                               |
| poetryのライブラリインストール           | `docker compose exec backend poetry install --no-root`                                                                                                            |
| poetryのライブラリ追加（開発環境用）     | `docker compose exec backend poetry add {lib} -D`                                                                                                                 |
| poetryのライブラリ追加                   | `docker compose exec backend poetry add {lib}`                                                                                                                    |
| バックエンド起動                         | `docker compose exec backend poetry run uvicorn app.main:app --reload`                                                                                            |
| マイグレーション                         | `docker compose exec backend poetry run python3 db.py`                                                                                                            |
| テスト                                   | `docker compose exec backend poetry run pytest`                                                                                                                   |
| テスト（カバレッジ表示）                 | `docker compose exec backend poetry run pytest --cov=app`                                                                                                         |
| テスト（カバレッジhtml出力）             | `docker compose exec backend poetry run pytest --cov=app -v --cov-report=html`                                                                                    |
| テスト（カバレッジhtml出力＋docsコピー） | `docker compose exec backend poetry run pytest --cov=app -v --cov-report=html && rsync -ahv ./backend/volumes/htmlcov/ ./docs/backend/cov --exclude '.gitignore'` |
| oss依存チェック                          | `docker compose exec backend pipdeptree`                                                                                                                          |
| ossライセンスチェック                    | `docker compose exec backend pip-licenses --order=license --format=csv --with-urls  --with-description`                                                           |
| ossライセンスチェック（csv出力）         | `docker compose exec backend pip-licenses --order=license --format=csv --with-urls  --with-description --output-file=/root/docs/backend/oss.csv`                  |
| ossライセンスチェック（html出力）        | `docker compose exec backend pip-licenses --order=license --format=html --with-urls  --with-description --output-file=/root/docs/backend/oss.html`                |
| lint, format, typecheck                  | `docker compose exec backend poetry run ruff .`                                                                                                                   |
| lint, format, typecheck                  | `docker compose exec backend poetry run ruff . --fix`                                                                                                             |
| ドキュメント生成（ER図）                 | `docker compose -f docker-compose-spy.yml run --rm schemaspy -configFile /config/schemaspy_sqlite.properties -debug`                                              |
| backend appディレクトリツリー出力        | `tree backend/volumes/app -I __pycache__`                                                                                                                         |

- 開発時
    - rootディレクトリを作業ディレクトリとする
    - `docker compose up` で起動
    - 各コマンドを必要に応じて実行する
        - バックエンド起動
        - ドキュメンテーション実行

- ドキュメンテーション
    - cov (pytest)
    - oss (pip-lisenses)
    - er (schemaspy)
    - api (redoc)

```
python db.py
sqlite3 dev.sqlite3
sqlite_web dev.sqlite3



# local実行
sls invoke local -f {function} --path {params.json}
sls invoke local -f api --path invoke.json

# デプロイ
sls deploy

# デプロイ一覧
sls deploy list --stage {env}

# 切り戻し (切り戻ししたときの元のものは消えない)
sls rollback --timestamp {timestamp} --stage {env}

# 全削除
sls remove --stage {env}
```

- [DockerでPoetryを使って環境構築しよう](https://book.st-hakky.com/hakky/try-poetry-on-docker/)
- [PythonでDDDやってみた](https://techtekt.persol-career.co.jp/entry/tech/231220_02)
    - 全体構成参考：細かいところは不完全なため実装変更する。


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
