#!/bin/bash

set -e

echo "Running build pytest_cov..."
docker compose exec backend poetry run pytest --cov=app -v --cov-report=html && rsync -ahv ./backend/volumes/htmlcov/ ./docs/backend/pytest_cov --exclude '.gitignore'
