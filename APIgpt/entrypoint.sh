#!/bin/bash

if [[ "$FLASK_ENV" != "production" ]]; then
  # Espera o MySQL iniciar apenas em desenvolvimento/local
  until mysql -h db -u root -pEnzo39824360 -e "SELECT 1"; do
    echo "Aguardando o MySQL iniciar..."
    sleep 1
  done
  echo "MySQL está pronto!"
fi

echo "Iniciando a aplicação Flask..."
flask run --host=0.0.0.0 --port=8000
