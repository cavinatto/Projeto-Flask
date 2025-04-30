from flask import Blueprint
from app.controllers import professor_controller

professor_bp = Blueprint('professor_bp', __name__)

professor_bp.route('/professores', methods=['POST'])(professor_controller.add_professor)
professor_bp.route('/professores', methods=['GET'])(professor_controller.get_professores)
professor_bp.route('/professores/<int:professor_id>', methods=['GET'])(professor_controller.get_professor_by_id)
professor_bp.route('/professores/<int:professor_id>', methods=['PUT'])(professor_controller.update_professor)
professor_bp.route('/professores/<int:professor_id>', methods=['DELETE'])(professor_controller.delete_professor)