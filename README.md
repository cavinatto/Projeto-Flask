# API de Gerenciamento Escolar

Esta API foi desenvolvida com o framework Flask utilizando o padrão arquitetural MVC (Model-View-Controller) para organizar de forma clara e escalável a lógica de negócio, rotas e estrutura de dados. Ela permite gerenciar alunos, professores e turmas de uma escola por meio de endpoints RESTful, oferecendo funcionalidades completas de cadastro, consulta, atualização e exclusão (CRUD).


## Tecnologias Utilizadas
- Python 3.11
- Flask
- Blueprints
- Pytest (Para testes unitários)


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

1. Para iniciar o servidor Flask execute app.py ou rode o comando:
   ```sh
   python app.py
   ```

2. A API estará disponível em: `http://127.0.0.1:5000/`


## Endpoints

### Alunos

| Método | Rota                | Descrição |
|---------|---------------------|------------|
| GET     | `/alunos`           | Retorna todos os alunos |
| GET     | `/alunos/<id>`      | Retorna um aluno específico |
| POST    | `/alunos`           | Cria um novo aluno |
| PUT     | `/alunos/<id>`      | Atualiza um aluno |
| DELETE  | `/alunos/<id>`      | Remove um aluno |

### Professores

| Método | Rota                | Descrição |
|---------|---------------------|------------|
| GET     | `/professores`      | Retorna todos os professores |
| GET     | `/professores/<id>` | Retorna um professor específico |
| POST    | `/professores`      | Cria um novo professor |
| PUT     | `/professores/<id>` | Atualiza um professor |
| DELETE  | `/professores/<id>` | Remove um professor |

### Turmas

| Método | Rota            | Descrição |
|---------|---------------|------------|
| GET     | `/turmas`     | Retorna todas as turmas |
| GET     | `/turmas/<id>`| Retorna uma turma específica |
| POST    | `/turmas`     | Cria uma nova turma |
| PUT     | `/turmas/<id>` | Atualiza uma turma |
| DELETE  | `/turmas/<id>` | Remove uma turma |

## Testando a API

Para rodar os testes unitários, utilize:

```sh
python -m pytest
```

Isso executa uma série de testes para validar o funcionamento correto da API.
