from flask import Blueprint
from app.controllers import aluno_controller

aluno_bp = Blueprint('aluno_bp', __name__)

aluno_bp.route('/alunos', methods=['POST'])(aluno_controller.add_aluno)
aluno_bp.route('/alunos', methods=['GET'])(aluno_controller.get_alunos)
aluno_bp.route('/alunos/<int:aluno_id>', methods=['GET'])(aluno_controller.get_aluno_by_id)
aluno_bp.route('/alunos/<int:aluno_id>', methods=['PUT'])(aluno_controller.update_aluno)
aluno_bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])(aluno_controller.delete_aluno)