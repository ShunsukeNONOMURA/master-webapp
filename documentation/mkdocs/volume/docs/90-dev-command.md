# コマンドチートシート
- rootディレクトリを作業ディレクトリとする
- exec経由実行をメインにしている
- `./scripts`以下にある程度まとめている
    - 検討中：poetry実行周りを`tool.poetry.scripts`に移管

| 操作                                     | コマンド                                                                                                                                                          |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| コンテナ起動                             | `docker compose up`                                                                                                                                               |
| poetryのライブラリインストール           | `docker compose exec backend poetry install --no-root`                                                                                                            |
| poetryのライブラリ追加（開発環境用）     | `docker compose exec backend poetry add {lib} -D`                                                                                                                 |
| poetryのライブラリ追加                   | `docker compose exec backend poetry add {lib}`                                                                                                                    |
| 開発用RDB初期化                          | `docker compose exec backend poetry run python3 ./migrate.py`                                                                                                     |
| 開発用バックエンド起動                   | `docker compose exec backend poetry run uvicorn app.main:app --reload`                                                                                            |
| テスト                                   | `docker compose exec backend poetry run pytest`                                                                                                                   |
| テスト（カバレッジ表示）                 | `docker compose exec backend poetry run pytest --cov=app`                                                                                                         |
| テスト（カバレッジhtml出力）             | `docker compose exec backend poetry run pytest --cov=app -v --cov-report=html`                                                                                    |
| テスト（カバレッジhtml出力＋docsコピー） | `docker compose exec backend poetry run pytest --cov=app -v --cov-report=html && rsync -ahv ./backend/volumes/htmlcov/ ./docs/backend/cov --exclude '.gitignore'` |
| oss依存チェック                          | `docker compose exec backend pipdeptree`                                                                                                                          |
| ossライセンスチェック                    | `docker compose exec backend pip-licenses --order=license --format=csv --with-urls  --with-description`                                                           |
| ossライセンスチェック（csv出力）         | `docker compose exec backend pip-licenses --order=license --format=csv --with-urls  --with-description --output-file=/root/docs/backend/oss.csv`                  |
| ossライセンスチェック（html出力）        | `docker compose exec backend pip-licenses --order=license --format=html --with-urls  --with-description --output-file=/root/docs/backend/oss.html`                |
| ruff(lint, format)                       | `docker compose exec backend poetry run ruff check .`                                                                                                             |
| ruff(lint, format) (強制fix)             | `docker compose exec backend poetry run ruff check . --fix --unsafe-fixes`                                                                                        |
| mypy(typecheck)                          | `docker compose exec backend poetry run mypy .`                                                                                                                   |
| ドキュメント生成（ER図）                 | `docker compose -f docker-compose-spy.yml run --rm schemaspy -configFile /config/schemaspy_sqlite.properties -debug`                                              |
| backend appディレクトリツリー出力        | `tree backend/volumes/app -I __pycache__`                                                                                                                         |