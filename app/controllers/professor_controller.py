from flask import request, jsonify
from app.models import professor_model

def add_professor():
    data = request.get_json()
    novo = professor_model.criar_professor(data)
    return jsonify(novo), 201

def get_professores():
    return jsonify(professor_model.listar_professores())

def get_professor_by_id(professor_id):
    prof = professor_model.buscar_professor_por_id(professor_id)
    if prof:
        return jsonify(prof)
    return jsonify({"erro": "Professor não encontrado"}), 404

def update_professor(professor_id):
    data = request.get_json()
    prof = professor_model.atualizar_professor(professor_id, data)
    if prof:
        return jsonify(prof)
    return jsonify({"erro": "Professor não encontrado"}), 404

def delete_professor(professor_id):
    professor_model.deletar_professor(professor_id)
    return jsonify({"mensagem": "Removido com sucesso"})
