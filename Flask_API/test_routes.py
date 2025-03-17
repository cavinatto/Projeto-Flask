import pytest
from app import create_app
from routes import professores, turmas, alunos

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()



# TESTES UNITÁRIOS PARA PROFESSORES
#CREATE
def test_create_professor(client):
    resposta = client.post('/professores', json={"nome": "Carlos Silva"})
    assert resposta.status_code == 201
    assert resposta.json == {"id": 1, "nome": "Carlos Silva"}

#READ
def test_get_professores(client):
    global professores
    professores.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    resposta = client.get('/professores')
    assert resposta.status_code == 200
    assert len(resposta.json) == 1

#UPDATE
def test_update_professor(client):
    global professores
    professores.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    resposta = client.put('/professores/1', json={"nome": "Carlos Souza"})
    assert resposta.status_code == 200
    assert resposta.json == {"id": 1, "nome": "Carlos Souza"}

#DELETE
def test_delete_professor(client):
    global professores
    professores.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    resposta = client.delete('/professores/1')
    
    assert resposta.status_code == 200
    assert resposta.json == {"mensagem": "Professor removido com sucesso"}
    assert client.get('/professores').json == []



# TESTES UNITÁRIOS PARA TURMAS
#CREATE
def test_create_turma(client):
    global turmas
    turmas.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    resposta = client.post('/turmas', json={"nome": "Matemática", "professor_id": 1})
    
    assert resposta.status_code == 201
    assert resposta.json == {"id": 1, "nome": "Matemática", "professor_id": 1}

#READ
def test_get_turmas(client):
    global turmas
    turmas.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    client.post('/turmas', json={"nome": "Matemática", "professor_id": 1})
    resposta = client.get('/turmas')

    assert resposta.status_code == 200
    assert len(resposta.json) == 1

#UPDATE
def test_update_turma(client):
    global turmas
    turmas.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    client.post('/turmas', json={"nome": "Matemática", "professor_id": 1})
    resposta = client.put('/turmas/1', json={"nome": "Física", "professor_id": 1})

    assert resposta.status_code == 200
    assert resposta.json == {"id": 1, "nome": "Física", "professor_id": 1}

#DELETE
def test_delete_turma(client):
    global turmas
    turmas.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    client.post('/turmas', json={"nome": "Matemática", "professor_id": 1})
    resposta = client.delete('/turmas/1')

    assert resposta.status_code == 200
    assert resposta.json == {"mensagem": "Turma removida com sucesso"}
    assert client.get('/turmas').json == []



# TESTES UNITÁRIOS PARA ALUNOS
#CREATE
def test_create_aluno(client):
    global alunos
    alunos.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    client.post('/turmas', json={"nome": "Matemática", "professor_id": 1})
    resposta = client.post('/alunos', json={"nome": "João", "turma_id": 1})

    assert resposta.status_code == 201
    assert resposta.json == {"id": 1, "nome": "João", "turma_id": 1}

#READ
def test_get_alunos(client):
    global alunos
    alunos.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    client.post('/turmas', json={"nome": "Matemática", "professor_id": 1})
    client.post('/alunos', json={"nome": "João", "turma_id": 1})
    resposta = client.get('/alunos')

    assert resposta.status_code == 200
    assert len(resposta.json) == 1

#UPDATE
def test_update_aluno(client):
    global alunos
    alunos.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    client.post('/turmas', json={"nome": "Matemática", "professor_id": 1})
    client.post('/alunos', json={"nome": "João", "turma_id": 1})
    resposta = client.put('/alunos/1', json={"nome": "Maria", "turma_id": 1})

    assert resposta.status_code == 200
    assert resposta.json == {"id": 1, "nome": "Maria", "turma_id": 1}

#DELETE
def test_delete_aluno(client):
    global alunos
    alunos.clear()

    client.post('/professores', json={"nome": "Carlos Silva"})
    client.post('/turmas', json={"nome": "Matemática", "professor_id": 1})
    client.post('/alunos', json={"nome": "João", "turma_id": 1})
    resposta = client.delete('/alunos/1')

    assert resposta.status_code == 200
    assert resposta.json == {"mensagem": "Aluno removido com sucesso"}
    assert client.get('/alunos').json == []