# OSS
主に利用しているOSSについて記述する。  
自動化できるところは自動化できるようにする。  
できるだけ一般知識で更新ができるように、ossは担げる場合は担ぐ方式を取る。  
テスト、解析、可視化のよう開発環境のみ必要になるものは特にOSSを担ぎたい。  

## 主要OSS一覧
| 機能                       | 依存                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------- |
| パッケージマネージャ       | [Poetry](https://python-poetry.org/)                                                                      |
| フレームワーク             | [FastAPI](https://fastapi.tiangolo.com/ja/)                                                               |
| ASGI                       | [FastAPI uvicorn](https://fastapi.tiangolo.com/ja/tutorial/#_1)                                           |
| CQRS対応                   | [FastAPI (CORS (オリジン間リソース共有))](https://fastapi.tiangolo.com/ja/tutorial/cors/#cors)            |
| バックグラウンドタスク     | [FastAPI (バックグラウンドタスク)](https://fastapi.tiangolo.com/ja/tutorial/background-tasks/)            |
| DI                         | [FastAPI (Depends)](https://fastapi.tiangolo.com/ja/tutorial/dependencies/)                               |
| ORM                        | [SQLModel](https://sqlmodel.tiangolo.com/)                                                                |
| RDB                        | [SQLite](https://www.sqlite.org/), [postgresql](https://www.postgresql.org/)                              |
| マイグレーション           | **検討中**：Alembic                                                                                       |
| Linter,Formatter           | [Ruff](https://docs.astral.sh/ruff/)                                                                      |
| 型チェック                 | [mypy](https://mypy.readthedocs.io/en/stable/#)                                                           |
| APIユニットテスト          | [Fastapi (TestClient)](https://fastapi.tiangolo.com/ja/tutorial/testing/)                                 |
| 負荷テスト                 | **検討中**：Locust                                                                                        |
| クラスドキュメンテーション | **検討中**：sphinx                                                                                        |
| APIドキュメンテーション    | [FastAPI (swagger, redoc)](https://fastapi.tiangolo.com/ja/features/)                                     |
| DDLドキュメンテーション    | [schemaspy](https://schemaspy.org/)                                                                       |
| OSSドキュメンテーション    | [pip-license](https://pypi.org/project/pip-licenses/), [pipdeptree](https://pypi.org/project/pipdeptree/) |
| MDドキュメンテーション     | [mkdocs](https://www.mkdocs.org/)  , [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)  |

## Poetry
[pyproject.toml](https://github.com/ShunsukeNONOMURA/webapp-fastapi-master/blob/main/backend/volumes/pyproject.toml)に下記の諸情報を記載し、実行環境を管理するもの。

- 依存OSS
- 静的解析設定

[参考：DockerでPoetryを使って環境構築しよう](https://book.st-hakky.com/hakky/try-poetry-on-docker/)

## FastAPI
- PythonWebフレームワーク
- ASGIサーバー(uvicornなど)経由で起動する
- [pydantic標準対応](https://fastapi.tiangolo.com/ja/python-types/?h=#pydantic)
    - 型チェックやバリデーションが可能
- [openapi標準対応](https://fastapi.tiangolo.com/ja/features/#_3)
    - swaggerやredocといった実行ツールやドキュメンテーションを自動生成
    - endpointの実装があればIF設計できる
- DI, CORS, バックグラウンドタスクあたりの実装も可能

## SQLModel
- FastAPIと開発元が同じsclalchemyのPydanticラッパー
- FastAPIとPydanticに対する親和性が高いので採用
- 基本的にはSQModelの提供機能（pydanticライクな記述）で設定可能だが、一部の細かい設定を行う場合はsqlalchemyの記述を利用する必要がある
