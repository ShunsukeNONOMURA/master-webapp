#!/bin/bash

set -e

echo "Running build license..."

# backend oss license
docker compose exec backend pip-licenses --order=license --format=csv --with-urls  --with-description --output-file=/root/docs/backend/oss.csv
docker compose exec backend pip-licenses --order=license --format=html --with-urls  --with-description --output-file=/root/docs/backend/oss.html

# dep tree
docker compose exec backend sh -c "pipdeptree > /root/docs/backend/dependencies.txt"
echo created path: /root/docs/backend/dependencies.txt