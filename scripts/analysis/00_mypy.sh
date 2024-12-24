#!/bin/bash

set -e

echo "Running type check (mypy)..."
docker compose exec backend poetry run mypy .
