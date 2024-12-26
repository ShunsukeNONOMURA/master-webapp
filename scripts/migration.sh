# 一度すべて削除する方式なので実行注意する
# db init
docker compose exec backend rm -rf migrations/versions
docker compose exec backend mkdir migrations/versions
docker compose exec backend rm dev.sqlite3 # sqlite削除

# migration
docker compose exec backend alembic revision --autogenerate
docker compose exec backend alembic upgrade head

docker compose exec backend python db.py

