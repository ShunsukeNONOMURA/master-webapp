# pytest
docker compose exec backend poetry run pytest --cov=app -v --cov-report=html && rsync -ahv ./backend/volumes/htmlcov/ ./docs/backend/pytest_cov --exclude '.gitignore'

# OSS
docker compose exec backend pip-licenses --order=license --format=csv --with-urls  --with-description --output-file=/root/docs/backend/oss.csv
docker compose exec backend pip-licenses --order=license --format=html --with-urls  --with-description --output-file=/root/docs/backend/oss.html

# ER
docker compose -f docker-compose-spy.yml run --rm schemaspy -configFile /config/config_postgres.properties -debug