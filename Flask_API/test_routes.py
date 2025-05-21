import unittest
from app import app
import json

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    # ---------------- Alunos ----------------

    def test_adicionar_aluno(self):
        # Primeiro, criar uma turma para associar
        resp_turma = self.client.post('/turmas', json={"nome": "Turma 1", "professor_id": 1})
        if resp_turma.status_code == 400:
            # se professor 1 não existe, cria um professor
            self.client.post('/professores', json={"nome": "Prof Teste"})
            resp_turma = self.client.post('/turmas', json={"nome": "Turma 1", "professor_id": 1})
        turma = resp_turma.get_json()

        resp = self.client.post('/alunos', json={"nome": "Aluno Teste", "turma_id": turma["id"]})
        self.assertEqual(resp.status_code, 201)
        self.assertIn("id", resp.get_json())

    def test_listar_alunos(self):
        resp = self.client.get('/alunos')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.get_json(), list)

    def test_buscar_aluno_por_id(self):
        # Adiciona aluno para buscar
        resp_add = self.client.post('/alunos', json={"nome": "Aluno Busca", "turma_id": 1})
        aluno_id = resp_add.get_json()["id"]
        resp = self.client.get(f'/alunos/{aluno_id}')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["id"], aluno_id)

    def test_atualizar_aluno(self):
        resp_add = self.client.post('/alunos', json={"nome": "Aluno Atualizar", "turma_id": 1})
        aluno_id = resp_add.get_json()["id"]
        resp = self.client.put(f'/alunos/{aluno_id}', json={"nome": "Aluno Atualizado", "turma_id": 1})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["nome"], "Aluno Atualizado")

    def test_remover_aluno(self):
        resp_add = self.client.post('/alunos', json={"nome": "Aluno Remover", "turma_id": 1})
        aluno_id = resp_add.get_json()["id"]
        resp = self.client.delete(f'/alunos/{aluno_id}')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("mensagem", resp.get_json())

    # -------------- Professores --------------

    def test_adicionar_professor(self):
        resp = self.client.post('/professores', json={"nome": "Professor Teste"})
        self.assertEqual(resp.status_code, 201)
        self.assertIn("id", resp.get_json())

    def test_listar_professores(self):
        resp = self.client.get('/professores')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.get_json(), list)

    def test_buscar_professor_por_id(self):
        resp_add = self.client.post('/professores', json={"nome": "Prof Busca"})
        prof_id = resp_add.get_json()["id"]
        resp = self.client.get(f'/professores/{prof_id}')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["id"], prof_id)

    def test_atualizar_professor(self):
        resp_add = self.client.post('/professores', json={"nome": "Prof Atualizar"})
        prof_id = resp_add.get_json()["id"]
        resp = self.client.put(f'/professores/{prof_id}', json={"nome": "Prof Atualizado"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["nome"], "Prof Atualizado")

    def test_remover_professor(self):
        resp_add = self.client.post('/professores', json={"nome": "Prof Remover"})
        prof_id = resp_add.get_json()["id"]
        resp = self.client.delete(f'/professores/{prof_id}')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("mensagem", resp.get_json())

    # -------------- Turmas --------------

    def test_adicionar_turma(self):
        # cria professor pra turma
        resp_prof = self.client.post('/professores', json={"nome": "Prof Turma"})
        prof_id = resp_prof.get_json()["id"]

        resp = self.client.post('/turmas', json={"nome": "Turma Teste", "professor_id": prof_id})
        self.assertEqual(resp.status_code, 201)
        self.assertIn("id", resp.get_json())

    def test_listar_turmas(self):
        resp = self.client.get('/turmas')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.get_json(), list)

    def test_buscar_turma_por_id(self):
        resp_prof = self.client.post('/professores', json={"nome": "Prof Busca Turma"})
        prof_id = resp_prof.get_json()["id"]

        resp_add = self.client.post('/turmas', json={"nome": "Turma Busca", "professor_id": prof_id})
        turma_id = resp_add.get_json()["id"]

        resp = self.client.get(f'/turmas/{turma_id}')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["id"], turma_id)

    def test_atualizar_turma(self):
        resp_prof = self.client.post('/professores', json={"nome": "Prof Atualizar Turma"})
        prof_id = resp_prof.get_json()["id"]

        resp_add = self.client.post('/turmas', json={"nome": "Turma Atualizar", "professor_id": prof_id})
        turma_id = resp_add.get_json()["id"]

        resp = self.client.put(f'/turmas/{turma_id}', json={"nome": "Turma Atualizada", "professor_id": prof_id})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["nome"], "Turma Atualizada")

    def test_remover_turma(self):
        resp_prof = self.client.post('/professores', json={"nome": "Prof Remover Turma"})
        prof_id = resp_prof.get_json()["id"]

        resp_add = self.client.post('/turmas', json={"nome": "Turma Remover", "professor_id": prof_id})
        turma_id = resp_add.get_json()["id"]

        resp = self.client.delete(f'/turmas/{turma_id}')
        self.assertEqual(resp.status_code, 200)
        self.assertIn("mensagem", resp.get_json())


if __name__ == "__main__":
    unittest.main()
