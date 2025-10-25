#!/bin/bash
set -euo pipefail

echo "🚀 Запускаем docker-compose..."
docker-compose up -d

echo "⏳ Ожидание готовности БД..."
until docker exec rt_postgres pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB} > /dev/null 2>&1; do
  sleep 2
done

echo "✅ БД готова. Выполняем тестовые запросы..."

docker exec rt_postgres psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f /test/queries.sql | tee /tmp/query_results.txt

if [ ${PIPESTATUS[0]} -ne 0 ]; then
  echo "❌ Ошибка при выполнении запросов"
  docker compose logs db
  exit 1
fi

echo "🎉 Все запросы выполнены успешно"
docker compose down -v