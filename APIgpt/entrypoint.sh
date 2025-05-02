#!/bin/bash

# Espera o MySQL estar pronto
until mysql -h db -u root -pEnzo39824360 -e "SELECT 1"; do
  echo "Aguardando o MySQL iniciar..."
  sleep 1
done

echo "MySQL está pronto! Iniciando a aplicação Flask..."
flask run --host=0.0.0.0 --port=8000