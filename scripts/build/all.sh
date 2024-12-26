#!/bin/bash

set -e

echo "Running all build docs tasks..."

./scripts/build/00_pytest_cov.sh
./scripts/build/01_redoc.sh
./scripts/build/02_license.sh
./scripts/build/10_er.sh
./scripts/build/20_mkdocs.sh

echo "All docs build docs completed successfully!"