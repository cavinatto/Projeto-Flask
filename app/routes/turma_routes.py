from flask import Blueprint
from app.controllers import turma_controller

turma_bp = Blueprint('turma_bp', __name__)

turma_bp.route('/turmas', methods=['POST'])(turma_controller.add_turma)
turma_bp.route('/turmas', methods=['GET'])(turma_controller.get_turmas)
turma_bp.route('/turmas/<int:turma_id>', methods=['GET'])(turma_controller.get_turma_by_id)
turma_bp.route('/turmas/<int:turma_id>', methods=['PUT'])(turma_controller.update_turma)
turma_bp.route('/turmas/<int:turma_id>', methods=['DELETE'])(turma_controller.delete_turma)