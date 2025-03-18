# Test Driven Development, conforme o roteiro dado no classroom

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
