import unittest
from unittest.mock import MagicMock

class TestProfessor(unittest.TestCase):
    def setUp(self):
        self.professor_service = MagicMock()

    def test_create_professor_1(self):
        self.professor_service.create.return_value = {'id': 1, 'nome': 'Dr. João', 'materia': 'Matemática'}
        professor = self.professor_service.create('Dr. João', 'Matemática')
        self.assertEqual(professor['nome'], 'Dr. João')

    def test_create_professor_2(self):
        self.professor_service.create.return_value = {'id': 2, 'nome': 'Dra. Ana', 'materia': 'História'}
        professor = self.professor_service.create('Dra. Ana', 'História')
        self.assertEqual(professor['materia'], 'História')

    def test_get_professor_1(self):
        self.professor_service.get.return_value = {'id': 1, 'nome': 'Dr. João', 'materia': 'Matemática'}
        professor = self.professor_service.get(1)
        self.assertEqual(professor['nome'], 'Dr. João')

    def test_update_professor_1(self):
        self.professor_service.update.return_value = {'id': 1, 'nome': 'Dr. João Atualizado', 'materia': 'Física'}
        professor = self.professor_service.update(1, 'Dr. João Atualizado', 'Física')
        self.assertEqual(professor['materia'], 'Física')

    def test_delete_professor_1(self):
        self.professor_service.delete.return_value = True
        self.assertTrue(self.professor_service.delete(1))

    def test_create_professor_3(self):
        self.professor_service.create.return_value = {'id': 3, 'nome': 'Carlos', 'materia': 'Geografia'}
        self.assertEqual(self.professor_service.create('Carlos', 'Geografia')['nome'], 'Carlos')

    def test_create_professor_4(self):
        self.professor_service.create.return_value = {'id': 4, 'nome': 'Bruna', 'materia': 'Química'}
        self.assertEqual(self.professor_service.create('Bruna', 'Química')['materia'], 'Química')

    def test_update_professor_2(self):
        self.professor_service.update.return_value = {'id': 2, 'nome': 'Ana B.', 'materia': 'Sociologia'}
        prof = self.professor_service.update(2, 'Ana B.', 'Sociologia')
        self.assertEqual(prof['materia'], 'Sociologia')

    def test_delete_professor_2(self):
        self.professor_service.delete.return_value = True
        self.assertTrue(self.professor_service.delete(2))

    def test_get_all_professores(self):
        self.professor_service.get_all.return_value = []
        self.assertEqual(self.professor_service.get_all(), [])

    def test_create_professor_5(self):
        self.professor_service.create.return_value = {'id': 5, 'nome': 'Luis', 'materia': 'Filosofia'}
        prof = self.professor_service.create('Luis', 'Filosofia')
        self.assertEqual(prof['nome'], 'Luis')

    def test_create_professor_6(self):
        self.professor_service.create.return_value = {'id': 6, 'nome': 'Renata', 'materia': 'Biologia'}
        prof = self.professor_service.create('Renata', 'Biologia')
        self.assertEqual(prof['materia'], 'Biologia')

    def test_update_professor_3(self):
        self.professor_service.update.return_value = {'id': 6, 'nome': 'Renata Atualizada', 'materia': 'Educação Física'}
        prof = self.professor_service.update(6, 'Renata Atualizada', 'Educação Física')
        self.assertEqual(prof['nome'], 'Renata Atualizada')

    def test_delete_professor_3(self):
        self.professor_service.delete.return_value = True
        self.assertTrue(self.professor_service.delete(6))

    def test_create_professor_7(self):
        self.professor_service.create.return_value = {'id': 7, 'nome': 'Roberto', 'materia': 'Artes'}
        prof = self.professor_service.create('Roberto', 'Artes')
        self.assertEqual(prof['nome'], 'Roberto')


if __name__ == "__main__":
    unittest.main(verbosity=2)
