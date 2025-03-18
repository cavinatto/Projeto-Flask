import pytest
from app import create_app  # Função para criar a app Flask
from routes import alunos  # Supondo que você tenha um arquivo routes.py

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

# Teste 000: Verificando GET /alunos
def test_get_alunos(client):
    resposta = client.get('/alunos')
    assert resposta.status_code == 200
    assert isinstance(resposta.json, list)  # Espera-se uma lista de alunos

# Teste 001: Criando um aluno com POST /alunos
def test_create_aluno(client):
    resposta = client.post('/alunos', json={"nome": "Marcos"})
    assert resposta.status_code == 201
    assert resposta.json == {"id": 1, "nome": "Marcos"}  # Verifica se o aluno foi criado corretamente

# Teste 002: Obtendo um aluno específico com GET /alunos/<id>
def test_get_aluno(client):
    client.post('/alunos', json={"nome": "Marcos"})  # Criar aluno
    resposta = client.get('/alunos/1')  # Buscar pelo aluno 1
    assert resposta.status_code == 200
    assert resposta.json == {"id": 1, "nome": "Marcos"}  # Verificando se o aluno retornado é o correto

# Teste 003: Resetando os dados com POST /reseta
def test_reseta(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.post('/reseta')  # Resetando dados
    assert resposta.status_code == 200
    assert len(client.get('/alunos').json) == 0  # Verificando se a lista de alunos está vazia

# Teste 004: Deletando um aluno com DELETE /alunos/<id>
def test_delete_aluno(client):
    client.post('/alunos', json={"nome": "Marcos"})  # Criar aluno
    resposta = client.delete('/alunos/1')  # Deletando aluno com id 1
    assert resposta.status_code == 200
    assert client.get('/alunos').json == []  # Verificando se a lista de alunos está vazia

# Teste 005: Editando um aluno com PUT /alunos/<id>
def test_update_aluno(client):
    client.post('/alunos', json={"nome": "Marcos"})  # Criar aluno
    resposta = client.put('/alunos/1', json={"nome": "José"})  # Alterar o nome do aluno
    assert resposta.status_code == 200
    assert resposta.json == {"id": 1, "nome": "José"}  # Verificando se o nome foi alterado corretamente

# Teste 006: Tentando acessar um aluno que não existe (GET)
def test_get_aluno_nao_existente(client):
    resposta = client.get('/alunos/15')  # Acessando aluno com id 15 que não existe
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "aluno nao encontrado"}

# Teste 007: Tentando criar aluno com id já existente
def test_create_aluno_id_existente(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.post('/alunos', json={"nome": "José"})  # Tentando criar um aluno com id já existente
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "id ja utilizada"}

# Teste 008a: Criando aluno sem nome (POST)
def test_create_aluno_sem_nome(client):
    resposta = client.post('/alunos', json={})  # Enviando aluno sem nome
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "aluno sem nome"}

# Teste 008b: Editando aluno sem nome (PUT)
def test_update_aluno_sem_nome(client):
    client.post('/alunos', json={"nome": "Marcos"})
    resposta = client.put('/alunos/1', json={})  # Tentando editar aluno sem nome
    assert resposta.status_code == 400
    assert resposta.json == {"erro": "aluno sem nome"}
