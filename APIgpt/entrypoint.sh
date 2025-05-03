#!/bin/bash

# Espera o MySQL do Railway estar pronto
until mysql -h "$MYSQL_HOST" -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SELECT 1" 2>/dev/null; do
  echo "Aguardando o MySQL iniciar..."
  sleep 2
done

echo "MySQL está pronto! Iniciando a aplicação Flask com gunicorn..."
exec gunicorn -b 0.0.0.0:${PORT:-8000} app:app
