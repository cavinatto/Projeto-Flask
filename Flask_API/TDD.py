# Test Driven Development, conforme o roteiro dado no classroom

'''
Cada aluno será representado por um dicionário JSON como o seguinte: 
{"id":1,"nome":"marcos"}

Testes 000 e 001:
Na URL /alunos, se o verbo for GET, 
retornaremos uma lista com um dicionário para cada aluno.

Na URL /alunos, com o verbo POST, ocorrerá a criação do aluno,
enviando um desses dicionários 

Teste 002
Na URL /alunos/<int:id>, se o verbo for GET, devolveremos o nome e id do aluno. 
(exemplo. /alunos/2 devolve o dicionário do aluno(a) de id 2)

Teste 003
Na URL /reseta, apagaremos a lista de alunos e professores (essa URL só atende o verbo POST e DELETE).

Teste 004
Na URL /alunos/<int:id>, se o verbo for DELETE, deletaremos o aluno.
(dica: procure lista.remove)

Teste 005
Na URL /alunos/<int:id>, se o verbo for PUT, 
editaremos o aluno, mudando seu nome. 
Para isso, o usuário vai enviar um dicionário 
com a chave nome, que deveremos processar

Se o usuário manda um dicionário {“nome”:”José”} para a url /alunos/40,
com o verbo PUT, trocamos o nome do usuário 40 para José

Tratamento de erros

Testes 006 a 008b: Erros de usuário darão um código de status 400, e retornarão um dicionário descrevendo o erro. 
No teste 006, tentamos fazer GET, PUT e DELETE na URL  /alunos/15, sendo que o aluno de id 15 não existe. Nesse caso, devemos retornar um código de status 400 e um dicionário {“erro”:'aluno nao encontrado'}
No teste 007, tentamos criar dois alunos com a mesma id. Nesse caso, devemos retornar um código de status 400 e um dicionário {‘erro’:'id ja utilizada'}
No teste 008a, tento enviar um aluno sem nome via post. Nesse caso, devemos retornar um código de status 400 e um dicionário {‘erro’:'aluno sem nome'}
No teste 008b, tento editar um aluno, usando o verbo put, mas mando um dicionário sem nome. Nesse caso, devemos retornar um código de status 400 e um dicionário {“erro”:'aluno sem nome'}
'''

import pytest
from app import create_app
from routes import alunos

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

# Teste 000: Verificando GET /alunos (Passou)
def test_get_alunos(client):
    resposta = client.get('/alunos')
    assert resposta.status_code == 200
    assert isinstance(resposta.json, list)

# Teste 001: Criando um aluno com POST /alunos (Passou)
def test_create_aluno(client):
    resposta = client.post('/alunos', json={"nome": "Marcos"})
    assert resposta.status_code == 201
    assert resposta.json == {"id": 1, "nome": "Marcos"}

# Teste 002: Obtendo um aluno específico com GET /alunos/<id> (Passou)
def test_get_aluno(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.get('/alunos/1')
    assert resposta.status_code == 200
    assert resposta.json == {"id": 1, "nome": "Marcos"}

# Teste 003: Resetando os dados com POST /reseta (Passou)
def test_reseta(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.post('/reseta')
    assert resposta.status_code == 200
    assert len(client.get('/alunos').json) == 0

# Teste 004: Deletando um aluno com DELETE /alunos/<id> (Passou)
def test_delete_aluno(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.delete('/alunos/1')
    assert resposta.status_code == 200
    assert client.get('/alunos').json == []

# Teste 005: Editando um aluno com PUT /alunos/<id> (Passou)
def test_update_aluno(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.put('/alunos/1', json={"nome": "José"})
    assert resposta.status_code == 200
    assert resposta.json == {"id": 1, "nome": "José"}

# Teste 006: Tentando acessar um aluno que não existe (GET) (Passou)
def test_get_aluno_nao_existente(client):
    resposta = client.get('/alunos/15')
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "aluno nao encontrado"}

# Teste 007: Tentando criar aluno com id já existente (Passou)
def test_create_aluno_id_existente(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.post('/alunos', json={"nome": "José"})
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "id ja utilizada"}

# Teste 008a: Criando aluno sem nome (POST) (Passou)
def test_create_aluno_sem_nome(client):
    resposta = client.post('/alunos', json={})
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "aluno sem nome"}

# Teste 008b: Editando aluno sem nome (PUT) (Passou)
def test_update_aluno_sem_nome(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.put('/alunos/1', json={})
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "aluno sem nome"}
