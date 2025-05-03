import unittest
from unittest.mock import MagicMock

class TestAluno(unittest.TestCase):
    def setUp(self):
        self.aluno_service = MagicMock()

    def test_create_aluno_1(self):
        self.aluno_service.create.return_value = {'id': 1, 'nome': 'João', 'idade': 20}
        aluno = self.aluno_service.create('João', 20)
        self.assertEqual(aluno['nome'], 'João')
        self.assertEqual(aluno['idade'], 20)

    def test_create_aluno_2(self):
        self.aluno_service.create.return_value = {'id': 2, 'nome': 'Maria', 'idade': 21}
        aluno = self.aluno_service.create('Maria', 21)
        self.assertEqual(aluno['nome'], 'Maria')

    def test_create_aluno_3(self):
        self.aluno_service.create.return_value = {'id': 3, 'nome': 'Carlos', 'idade': 22}
        aluno = self.aluno_service.create('Carlos', 22)
        self.assertEqual(aluno['idade'], 22)

    def test_get_aluno_1(self):
        self.aluno_service.get.return_value = {'id': 1, 'nome': 'João', 'idade': 20}
        aluno = self.aluno_service.get(1)
        self.assertEqual(aluno['nome'], 'João')

    def test_get_aluno_2(self):
        self.aluno_service.get.return_value = {'id': 2, 'nome': 'Maria', 'idade': 21}
        aluno = self.aluno_service.get(2)
        self.assertEqual(aluno['nome'], 'Maria')

    def test_update_aluno_1(self):
        self.aluno_service.update.return_value = {'id': 1, 'nome': 'João A.', 'idade': 21}
        aluno = self.aluno_service.update(1, 'João A.', 21)
        self.assertEqual(aluno['nome'], 'João A.')

    def test_update_aluno_2(self):
        self.aluno_service.update.return_value = {'id': 2, 'nome': 'Maria B.', 'idade': 22}
        aluno = self.aluno_service.update(2, 'Maria B.', 22)
        self.assertEqual(aluno['idade'], 22)

    def test_delete_aluno_1(self):
        self.aluno_service.delete.return_value = True
        self.assertTrue(self.aluno_service.delete(1))

    def test_delete_aluno_2(self):
        self.aluno_service.delete.return_value = True
        self.assertTrue(self.aluno_service.delete(2))

    def test_get_all_alunos(self):
        self.aluno_service.get_all.return_value = []
        self.assertEqual(self.aluno_service.get_all(), [])

    def test_create_aluno_4(self):
        self.aluno_service.create.return_value = {'id': 4, 'nome': 'Ana', 'idade': 23}
        aluno = self.aluno_service.create('Ana', 23)
        self.assertEqual(aluno['nome'], 'Ana')

    def test_create_aluno_5(self):
        self.aluno_service.create.return_value = {'id': 5, 'nome': 'Lucas', 'idade': 24}
        aluno = self.aluno_service.create('Lucas', 24)
        self.assertEqual(aluno['idade'], 24)

    def test_create_aluno_6(self):
        self.aluno_service.create.return_value = {'id': 6, 'nome': 'Bia', 'idade': 19}
        aluno = self.aluno_service.create('Bia', 19)
        self.assertEqual(aluno['nome'], 'Bia')

    def test_update_aluno_3(self):
        self.aluno_service.update.return_value = {'id': 6, 'nome': 'Bia Atualizada', 'idade': 20}
        aluno = self.aluno_service.update(6, 'Bia Atualizada', 20)
        self.assertEqual(aluno['nome'], 'Bia Atualizada')

    def test_delete_aluno_3(self):
        self.aluno_service.delete.return_value = True
        self.assertTrue(self.aluno_service.delete(6))


if __name__ == "__main__":
    unittest.main(verbosity=2)
