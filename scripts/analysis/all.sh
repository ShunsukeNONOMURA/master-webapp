#!/bin/bash
# 検証のみ用途

set -e

echo "Running all analysis tasks..."

./scripts/analysis/00_mypy.sh
./scripts/analysis/01_ruff.sh
./scripts/analysis/10_pytest.sh

echo "All analysis tasks completed successfully!"



# set -e

# # スクリプト自身のディレクトリを取得
# SCRIPT_DIR=$(dirname "$(realpath "$0")")

# echo "Running all $SCRIPT_DIR tasks..."

# # 実行可能な*.shスクリプトを探して順次実行
# find "$SCRIPT_DIR" -type f -name "*.sh" ! -name "all.sh" | sort | while read -r file; do
#   echo "Executing $file..."
#   "$file"
# done

# echo "All analysis tasks completed successfully!"