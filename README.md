# API de Gestão Para Turmas

![Deploy](https://img.shields.io/badge/deploy-render-green)

Esta é uma API RESTful desenvolvida com Flask, utilizando MySQL como banco de dados, com suporte a Swagger (OpenAPI), Docker e deploy gratuito no Render (backend) e Railway (banco de dados).

## 📚 Funcionalidades

- CRUD de Alunos
- CRUD de Professores
- CRUD de Turmas
- Documentação interativa via Swagger

## 🚀 Deploy

A API está disponível em produção em:

🔗 [https://projetoflask-pu4h.onrender.com/docs](https://projetoflask-pu4h.onrender.com/docs)

## ⚙️ Tecnologias

- Python 3.9
- Flask 3.1
- Flask-RestX
- Flask-SQLAlchemy
- PyMySQL
- Docker
- MySQL (Local)

## 📥 Clonando o projeto

```bash
git clone git clone -b Backup https://github.com/cavinatto/ProjetoFlask.git
cd APIgpt
docker-compose up --build
```

## 🐋 Executando localmente com Docker

```bash
docker-compose up --build
```

- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- Endpoints: por exemplo, [http://localhost:8000/api/professores](http://localhost:8000/api/professores)

## 🧪 Rodando os testes

```bash
python -m unittest discover tests
```

## 📂 Estrutura do Projeto

```bash
APIgpt/
│
├── alunos/
│   ├── alunos_model.py
│   └── alunos_routes.py
│
├── professores/
│   ├── professores_model.py
│   └── professores_routes.py
│
├── turmas/
│   ├── turmas_model.py
│   └── turmas_routes.py
│
├── swagger/
│   ├── namespaces/
│   │   ├── aluno_namespace.py
│   │   ├── professor_namespace.py
│   │   └── turma_namespace.py
│   ├── swagger_config.py
│   └── __init__.py
│
├── tests/
│   ├── test_aluno.py
│   ├── test_professor.py
│   └── test_turma.py
│
├── config.py
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── entrypoint.sh
```

## 📝 Observações

- Em produção, o banco de dados é fornecido pelo Railway.
- Em ambiente local, o banco é iniciado via `docker-compose` com MySQL 5.7.
- Certifique-se de criar um arquivo `.env` com suas variáveis locais se necessário.

```env
# .env (exemplo)
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=1234
DB_NAME=escola
```

---
