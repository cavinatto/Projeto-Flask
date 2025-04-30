from flask import request, jsonify
from app.models import aluno_model

def add_aluno():
    data = request.get_json()
    novo = aluno_model.criar_aluno(data)
    return jsonify(novo), 201

def get_alunos():
    return jsonify(aluno_model.listar_alunos())

def get_aluno_by_id(aluno_id):
    aluno = aluno_model.buscar_aluno_por_id(aluno_id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

def update_aluno(aluno_id):
    data = request.get_json()
    aluno = aluno_model.atualizar_aluno(aluno_id, data)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

def delete_aluno(aluno_id):
    aluno_model.deletar_aluno(aluno_id)
    return jsonify({"mensagem": "Removido com sucesso"})