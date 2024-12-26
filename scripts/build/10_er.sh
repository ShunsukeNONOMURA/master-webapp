#!/bin/bash
# schemaspy経由での可視化であるのでconverter/schemaspyの構成を使っていることに注意する

set -e

echo "Running build er..."

# 既存のドキュメントを削除
rm -rf ../docs/rdb/schemaspy/*

# postgresql
docker compose -f docker-compose-spy.yml run --rm schemaspy -configFile /config/config_postgres.properties -debug -nopages
