# テスト
- 静的解析テスト、ユニットテストまで搭載
    - 本当はcommit時に自動テストとかできると良い
- E2Eテスト、負荷テストが現在ない

## 静的解析テスト
- ruff (linters + formatters) 
- mypy（typecheck）

### Ruff
- Linter/Formatter
- flake8 + black に代わる静的解析ツール
- [mypyなどの型チェッカーと組み合わせることが推奨される](https://docs.astral.sh/ruff/faq/#how-does-ruff-compare-to-mypy-or-pyright-or-pyre)
- 設定はpyproject.tomlを参照

設定例

```toml
[tool.ruff]
target-version = "py313"
lint.select = [
    "ALL"
]
lint.ignore = [
    "E501",    # pycodestyle Error: line-too-long
    "D100",    # pydocstyle: Missing docstring in public module
    "D101",    # pydocstyle: Missing docstring in public class
    "D102",    # pydocstyle: Missing docstring in public method
    "D103",    # pydocstyle: Missing docstring in public function
    "D104",    # pydocstyle: Missing docstring in public package
    "D105",    # pydocstyle: Missing docstring in magic method
    "D107",    # pydocstyle: Missing docstring in __init__
    "D400",    # pydocstyle: First line should end with a period
    "UP040",   # pyupgrade: non-pep695-type-alias  # TODO: mypyがPEP 695 type aliasesに対応したら有効にする
    "COM812",  # flake8-commas: missing-trailing-comma  # ruff formatterとコンフリクトする
    "ISC001",  # flake8-implicit-str-concat: single-line-implicit-string-concatenation # ruff formatterとコンフリクトする
    "TD003",   # flake8-todos: missing-todo-link  # TODO: ある程度モジュールが完成したら有効にする
    "FIX002",  # flake8-fixme: line-contains-todo # TODO: ある程度モジュールが完成したら有効にする
    "ERA001",  # eradicate: commented-out-code  # TODO: ある程度モジュールが完成したら有効にする
    
    "D203",    # （D211と競合）クラス docstring の前に空行を追加しない。
    "D212",    # （D213と競合）複数行の docstring の最初の行を概要にしない。

    "RUF001",  # 全角記号など`ambiguous unicode character`を許容
    "RUF002",  # 全角記号など`ambiguous unicode character`を許容
    "RUF003",  # 全角記号など`ambiguous unicode character`を許容
    "F403",    # from module import * を許容
    "T20",     # flake8-print # TODO print検出したい場合に有効化する。
]
lint.fixable = ["ALL"]

# Exclude a variety of commonly ignored directories.
exclude = [".venv", "venv", "tests/"]

[tool.ruff.lint.flake8-bugbear]
# FastAPI仕様の"B008"対策
extend-immutable-calls = ["fastapi.Depends", "fastapi.params.Depends", "fastapi.Query", "fastapi.params.Query"]

[tool.ruff.lint.pep8-naming]
# pydanticのvalidatorによる"N805"対応
classmethod-decorators = ["classmethod", "pydantic.validator"]
```

- select.Allなので基本的には全部適用。一部無視。
    - [参考：Ruff Rules](https://docs.astral.sh/ruff/rules/)
- その他諸設定
    - pydanticとFastapi対応
    - ruffの実行対象の設定

### mypy
設定例

```toml
[tool.mypy]
# チェックするファイルまたはディレクトリを指定
files = ["./app", "./migrations"]

# 無視したいファイルやディレクトリ
exclude = "^(\\.venv|\\.env|build|dist|__pycache__|tests/)"

# 型チェックを厳密にする
strict = true

# 型が見つからない場合のエラーを無効化
ignore_missing_imports = true

# 未使用の型ヒントを警告
warn_unused_ignores = true

# pydantic用の設定追加
plugins = ["pydantic.mypy"]
```

## ユニットテスト
- pytest

### pytest
- ユニットテストを行うツール
- APIテストは[Fastapi (TestClient)](https://fastapi.tiangolo.com/ja/tutorial/testing/)  経由で実行可能
- pytest-covと合わせてカバレッジ出力を行う
- プレゼンレイヤでのテストを主に作成し、pytest-covが100%に近くなるようにしておくことでデグレ影響をチェックして変更性を担保する。
- あまり本質的ではないcoverageの省略

設定例

```toml
[tool.pytest.ini_options]
filterwarnings = [
    "ignore::DeprecationWarning" # Deprecatedによる警告を無視する
]

[tool.coverage.report]
# 以下の項目についてのcoverageをスキップ
exclude_lines = [
    "pass",
    "raise NotImplementedError",
    "if TYPE_CHECKING:",
]
```


