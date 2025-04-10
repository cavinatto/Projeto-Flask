from flask import Blueprint
from app.controllers import professor_controller, turma_controller, aluno_controller

bp = Blueprint('routes', __name__)

# Professores
bp.route('/professores', methods=['POST'])(professor_controller.add_professor)
bp.route('/professores', methods=['GET'])(professor_controller.get_professores)
bp.route('/professores/<int:professor_id>', methods=['GET'])(professor_controller.get_professor_by_id)
bp.route('/professores/<int:professor_id>', methods=['PUT'])(professor_controller.update_professor)
bp.route('/professores/<int:professor_id>', methods=['DELETE'])(professor_controller.delete_professor)

# Turmas
bp.route('/turmas', methods=['POST'])(turma_controller.add_turma)
bp.route('/turmas', methods=['GET'])(turma_controller.get_turmas)
bp.route('/turmas/<int:turma_id>', methods=['GET'])(turma_controller.get_turma_by_id)
bp.route('/turmas/<int:turma_id>', methods=['PUT'])(turma_controller.update_turma)
bp.route('/turmas/<int:turma_id>', methods=['DELETE'])(turma_controller.delete_turma)

# Alunos
bp.route('/alunos', methods=['POST'])(aluno_controller.add_aluno)
bp.route('/alunos', methods=['GET'])(aluno_controller.get_alunos)
bp.route('/alunos/<int:aluno_id>', methods=['GET'])(aluno_controller.get_aluno_by_id)
bp.route('/alunos/<int:aluno_id>', methods=['PUT'])(aluno_controller.update_aluno)
bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])(aluno_controller.delete_aluno)