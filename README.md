# API de Gerenciamento Escolar

Esta API permite gerenciar alunos, professores e turmas de uma escola de forma simples.

## Tecnologias Utilizadas
- Python 3.11
- Flask
- Pytest (para testes unitários)

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/cavinatto/Projeto-Flask
   cd Projeto-Flask
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Executando a API

1. Inicie o servidor Flask:
   ```sh
   python app.py
   ```
2. A API estará disponível em: `http://127.0.0.1:5000/`

## Endpoints

### Alunos

| Método | Rota                | Descrição |
|---------|---------------------|------------|
| GET     | `/alunos`           | Retorna todos os alunos |
| POST    | `/alunos`           | Cria um novo aluno |
| PUT     | `/alunos/<id>`      | Atualiza um aluno |
| DELETE  | `/alunos/<id>`      | Remove um aluno |

### Professores

| Método | Rota                | Descrição |
|---------|---------------------|------------|
| GET     | `/professores`      | Retorna todos os professores |
| POST    | `/professores`      | Cria um novo professor |
| PUT     | `/professores/<id>` | Atualiza um professor |
| DELETE  | `/professores/<id>` | Remove um professor |

### Turmas

| Método | Rota            | Descrição |
|---------|---------------|------------|
| GET     | `/turmas`     | Retorna todas as turmas |
| POST    | `/turmas`     | Cria uma nova turma |
| PUT     | `/turmas/<id>` | Atualiza uma turma |
| DELETE  | `/turmas/<id>` | Remove uma turma |

## Testando a API

Para rodar os testes unitários, utilize:

```sh
python -m pytest
```

Isso executa uma série de testes para validar o funcionamento correto da API.
