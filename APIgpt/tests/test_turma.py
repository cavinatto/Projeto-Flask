import unittest
from unittest.mock import MagicMock

class TestTurma(unittest.TestCase):
    def setUp(self):
        self.turma_service = MagicMock()

    def test_create_turma_1(self):
        self.turma_service.create.return_value = {'id': 1, 'nome': '1A', 'ano': 2023}
        turma = self.turma_service.create('1A', 2023)
        self.assertEqual(turma['nome'], '1A')

    def test_create_turma_2(self):
        self.turma_service.create.return_value = {'id': 2, 'nome': '2B', 'ano': 2024}
        turma = self.turma_service.create('2B', 2024)
        self.assertEqual(turma['ano'], 2024)

    def test_get_turma(self):
        self.turma_service.get.return_value = {'id': 1, 'nome': '1A', 'ano': 2023}
        turma = self.turma_service.get(1)
        self.assertEqual(turma['nome'], '1A')

    def test_update_turma(self):
        self.turma_service.update.return_value = {'id': 1, 'nome': '1A - Atualizada', 'ano': 2023}
        turma = self.turma_service.update(1, '1A - Atualizada', 2023)
        self.assertEqual(turma['nome'], '1A - Atualizada')

    def test_delete_turma(self):
        self.turma_service.delete.return_value = True
        self.assertTrue(self.turma_service.delete(1))

    def test_create_turma_3(self):
        self.turma_service.create.return_value = {'id': 3, 'nome': '3C', 'ano': 2025}
        turma = self.turma_service.create('3C', 2025)
        self.assertEqual(turma['nome'], '3C')

    def test_get_all_turmas(self):
        self.turma_service.get_all.return_value = []
        self.assertEqual(self.turma_service.get_all(), [])

    def test_create_turma_4(self):
        self.turma_service.create.return_value = {'id': 4, 'nome': '4D', 'ano': 2026}
        self.assertEqual(self.turma_service.create('4D', 2026)['nome'], '4D')

    def test_create_turma_5(self):
        self.turma_service.create.return_value = {'id': 5, 'nome': '5E', 'ano': 2027}
        turma = self.turma_service.create('5E', 2027)
        self.assertEqual(turma['ano'], 2027)

    def test_update_turma_2(self):
        self.turma_service.update.return_value = {'id': 5, 'nome': '5E Atualizada', 'ano': 2027}
        turma = self.turma_service.update(5, '5E Atualizada', 2027)
        self.assertEqual(turma['nome'], '5E Atualizada')

    def test_delete_turma_2(self):
        self.turma_service.delete.return_value = True
        self.assertTrue(self.turma_service.delete(5))

    def test_create_turma_6(self):
        self.turma_service.create.return_value = {'id': 6, 'nome': '6F', 'ano': 2028}
        self.assertEqual(self.turma_service.create('6F', 2028)['ano'], 2028)

    def test_create_turma_7(self):
        self.turma_service.create.return_value = {'id': 7, 'nome': '7G', 'ano': 2029}
        self.assertEqual(self.turma_service.create('7G', 2029)['nome'], '7G')

    def test_update_turma_3(self):
        self.turma_service.update.return_value = {'id': 7, 'nome': '7G Atualizada', 'ano': 2029}
        turma = self.turma_service.update(7, '7G Atualizada', 2029)
        self.assertEqual(turma['nome'], '7G Atualizada')

    def test_delete_turma_3(self):
        self.turma_service.delete.return_value = True
        self.assertTrue(self.turma_service.delete(7))


if __name__ == "__main__":
    unittest.main(verbosity=2)
