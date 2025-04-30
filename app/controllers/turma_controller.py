from flask import request, jsonify
from app.models import turma_model

def add_turma():
    data = request.get_json()
    nova = turma_model.criar_turma(data)
    if nova:
        return jsonify(nova), 201
    return jsonify({"erro": "Professor não encontrado"}), 400

def get_turmas():
    return jsonify(turma_model.listar_turmas())

def get_turma_by_id(turma_id):
    turma = turma_model.buscar_turma_por_id(turma_id)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

def update_turma(turma_id):
    data = request.get_json()
    turma = turma_model.atualizar_turma(turma_id, data)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

def delete_turma(turma_id):
    turma_model.deletar_turma(turma_id)
    return jsonify({"mensagem": "Removida com sucesso"})
