# OSS

## 主要OSS
| 機能                       | 依存                                                                                                     |
| -------------------------- | -------------------------------------------------------------------------------------------------------- |
| パッケージマネージャ       | [Poetry](https://python-poetry.org/)                                                                     |
| フレームワーク             | [FastAPI](https://fastapi.tiangolo.com/ja/)                                                              |
| ASGI                       | uvicorn                                                                                                  |
| DI                         | [FastAPI (Depends)](https://fastapi.tiangolo.com/ja/tutorial/dependencies/)                              |
| ORM                        | [SQLModel](https://sqlmodel.tiangolo.com/)                                                               |
| RDB                        | [SQLite](https://www.sqlite.org/), [postgresql](https://www.postgresql.org/)                             |
| マイグレーション           | **検討中**：Alembic                                                                                      |
| Linter,Formatter           | [Ruff](https://docs.astral.sh/ruff/https://docs.astral.sh/ruff/)                                         |
| 型チェック                 | mypy                                                                                                     |
| APIテスト                  | [Fastapi (TestClient)](https://fastapi.tiangolo.com/ja/tutorial/testing/)                                |
| 負荷テスト                 | **検討中**：Locust?                                                                                      |
| クラスドキュメンテーション | **検討中**：sphinx                                                                                       |
| APIドキュメンテーション    | [FastAPI (swagger, redoc)](https://fastapi.tiangolo.com/ja/features/)                                    |
| DDLドキュメンテーション    | [schemaspy](https://schemaspy.org/)                                                                      |
| OSSドキュメンテーション    | pip-license, pipdeptree                                                                                  |
| MDドキュメンテーション     | [mkdocs](https://www.mkdocs.org/)  , [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) |

できるだけ一般知識で更新ができるように、独自実装せずにossは担げる場合は担ぐ。

## OSSライセンス一覧
| ライセンス                           | コピーレフト                                |
| ------------------------------------ | ------------------------------------------- |
| BSD License                          | 非該当                                      |
| MIT License                          | 非該当                                      |
| Apache Software License              | 非該当                                      |
| Mozilla Public License 2.0 (MPL 2.0) | OSSを改変した場合、改変箇所の公開義務が発生 |