from flask import Blueprint, request, jsonify
from .professores_model import listar_professores, adicionar_professor, professor_por_id, atualizar_professor, excluir_professor

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = listar_professores()
    return jsonify(professores)

@professores_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return jsonify(professor)
    except Exception:
        return jsonify({"message": "Professor não encontrado"}), 404

@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    response, status_code = adicionar_professor(data)
    return jsonify(response), status_code

@professores_blueprint.route('/professores/<int:id_professor>', methods=['PUT'])
def update_professor(id_professor):
    data = request.json
    try:
        professor = professor_por_id(id_professor)
        if not professor:
            return jsonify({"message": "Professor não encontrado"}), 404
        atualizar_professor(id_professor, data)
        return jsonify(data), 200
    except Exception:
        return jsonify({"message": "Professor não encontrado"}), 404

@professores_blueprint.route('/professores/<int:id_professor>', methods=['DELETE'])
def delete_professor(id_professor):
    try:
        excluir_professor(id_professor)
        return jsonify({"message": "Professor excluído com sucesso"}), 200
    except Exception:
        return jsonify({"message": "Professor não encontrado"}), 404
