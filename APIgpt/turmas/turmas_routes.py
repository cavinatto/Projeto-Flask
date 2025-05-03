from flask import Blueprint, request, jsonify
from .turmas_model import listar_turmas, adicionar_turma, turma_por_id, atualizar_turma, excluir_turma

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = listar_turmas()
    return jsonify(turmas)

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return jsonify(turma)
    except Exception:
        return jsonify({"message": "Turma não encontrada"}), 404

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    data = request.json
    response, status_code = adicionar_turma(data)
    return jsonify(response), status_code

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['PUT'])
def update_turma(id_turma):
    data = request.json
    try:
        turma = turma_por_id(id_turma)
        if not turma:
            return jsonify({"message": "Turma não encontrada"}), 404
        atualizar_turma(id_turma, data)
        return jsonify(data), 200
    except Exception:
        return jsonify({"message": "Turma não encontrada"}), 404

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['DELETE'])
def delete_turma(id_turma):
    try:
        excluir_turma(id_turma)
        return jsonify({"message": "Turma excluída com sucesso"}), 200
    except Exception:
        return jsonify({"message": "Turma não encontrada"}), 404
    