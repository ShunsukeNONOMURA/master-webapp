#!/bin/bash

set -e

# オプションが渡されていれば、それを使う
# 例：--unsafe-fixes --fix のとき修正をすべて行う
# ./scripts/backend/analysis/ruff --unsafe-fixes --fix
echo "Running static analysis (ruff)..."
docker compose exec backend poetry run ruff check . "$@"