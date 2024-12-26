#!/bin/bash

set -e

echo "Running build mkdocs..."
docker compose exec mkdocs mkdocs build