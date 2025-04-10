import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

# --- PROFESSORES ---
def test_add_professor(client):
    res = client.post('/professores', json={"nome": "Prof. João"})
    assert res.status_code == 201

def test_get_professores(client):
    res = client.get('/professores')
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_get_professor_por_id_nao_existente(client):
    res = client.get('/professores/999')
    assert res.status_code == 404 or res.status_code == 400

def test_update_professor(client):
    client.post('/professores', json={"nome": "Prof. Ana"})
    res = client.put('/professores/1', json={"nome": "Prof. Ana Maria"})
    assert res.status_code == 200
    assert res.get_json()["nome"] == "Prof. Ana Maria"

def test_delete_professor(client):
    client.post('/professores', json={"nome": "Prof. Pedro"})
    res = client.delete('/professores/2')
    assert res.status_code == 200

def test_get_professor_por_id(client):
    response_post = client.post('/professores', json={"nome": "Professor X"})
    assert response_post.status_code == 201
    professor = response_post.get_json()

    response_get = client.get(f'/professores/{professor["id"]}')
    assert response_get.status_code == 200
    assert response_get.get_json()["id"] == professor["id"]

# --- TURMAS ---
def test_add_turma_com_professor_existente(client):
    client.post('/professores', json={"nome": "Prof. Carlos"})
    res = client.post('/turmas', json={"nome": "Turma A", "professor_id": 3})
    assert res.status_code == 201

def test_add_turma_com_professor_inexistente(client):
    res = client.post('/turmas', json={"nome": "Turma B", "professor_id": 999})
    assert res.status_code == 400

def test_get_turmas(client):
    res = client.get('/turmas')
    assert res.status_code == 200

def test_update_turma(client):
    client.post('/turmas', json={"nome": "Turma C", "professor_id": 3})
    res = client.put('/turmas/1', json={"nome": "Turma C+", "professor_id": 3})
    assert res.status_code == 200

def test_delete_turma(client):
    res = client.delete('/turmas/1')
    assert res.status_code == 200

# --- ALUNOS ---
def test_add_aluno(client):
    client.post('/turmas', json={"nome": "Turma D", "professor_id": 3})
    res = client.post('/alunos', json={"nome": "Maria", "turma_id": 2})
    assert res.status_code == 201

def test_get_alunos(client):
    res = client.get('/alunos')
    assert res.status_code == 200

def test_update_aluno(client):
    client.post('/alunos', json={"nome": "João", "turma_id": 2})
    res = client.put('/alunos/1', json={"nome": "João Pedro", "turma_id": 2})
    assert res.status_code == 200

def test_delete_aluno(client):
    res = client.delete('/alunos/1')
    assert res.status_code == 200
