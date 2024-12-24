#!/bin/bash

set -e

# RDBデータを一度削除する場合があるので実行に注意すること
echo "Running migrate..."
docker compose exec backend poetry run python3 ./migrate.py "$@"