#!/bin/bash

set -e

echo "Running tests (pytest)..."
docker compose exec backend poetry run pytest --cov=app -v