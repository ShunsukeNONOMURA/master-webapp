
# master webapp
webアプリ開発用のマスタ。
できるだけ一般知識で更新ができるように、独自実装せずにossは担げる場合は担ぐ方針。

## Links
- https://github.com/ShunsukeNONOMURA/master-webapp
- https://shunsukenonomura.github.io/master-webapp/backend/api.html
- https://shunsukenonomura.github.io/master-webapp/backend/oss.html
- https://shunsukenonomura.github.io/master-webapp/backend/cov/index.html
- https://shunsukenonomura.github.io/master-webapp/rdb/schemaspy/index.html
- https://shunsukenonomura.github.io/mkdocs-development/volume/site/0400-example-ddd.html

## 構成
| サービス | 主要ライブラリ |
| -------- | -------------- |
| backend  | fastapi        |
| frontend | vite           |
| rdb      | postgresql     |

## backend
| 基本機能 | ライブラリ |
| -------- | ---------- |
| API      | fastapi    |
| lambda   | sls        |
| doc      | fastapi    |
| test     | pytest     |

| 機能             | 依存                   |
| ---------------- | ---------------------- |
| フレームワーク   | FastAPI                |
| アーキテクチャ   | オニオンアーキテクチャ |
| DB               | SQLite                 |
| テスト           | pytest                 |
| Linter,Formatter | ruff                   |
| マイグレーション | SQLModel, Alembic      |

## backend構成
| パス               | 役割                               |
| ------------------ | ---------------------------------- |
| app/core           | 共通で利用するモジュールなどを配置 |
| app/ddd            | DDD（ドメイン駆動設計）を表現する  |
| app/main.py        | 起動ファイル                       |
| migrations         | ORMやマイグレーション              |
| tests              | test関連                           |
| pyproject.toml     | poetry設定                         |

## コマンドシート
| 操作                                     | コマンド                                                                                                                                                          |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| コンテナ起動                             | `docker compose up`                                                                                                                                               |
| poetryのライブラリインストール           | `docker compose exec backend poetry install --no-root`                                                                                                            |
| poetryのライブラリ追加（開発環境用）     | `docker compose exec backend poetry add {lib} -D`                                                                                                                 |
| poetryのライブラリ追加                   | `docker compose exec backend poetry add {lib}`                                                                                                                    |
| バックエンド起動                         | `docker compose exec backend poetry run uvicorn app.main:app --reload`                                                                                            |
| マイグレーション                         | ``                                                                                                                                                                |
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

- []()
- [DockerでPoetryを使って環境構築しよう](https://book.st-hakky.com/hakky/try-poetry-on-docker/)
- [PythonでDDDやってみた](https://techtekt.persol-career.co.jp/entry/tech/231220_02)