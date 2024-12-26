#!/bin/bash

set -e

echo "Running build redoc..."
docker compose exec backend poetry run python3 build_redoc.py