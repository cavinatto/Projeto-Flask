from flask import request, jsonify
from app.models.aluno_model import alunos

def add_aluno():
    data = request.get_json()
    novo = {
        "id": len(alunos) + 1,
        "nome": data["nome"],
        "turma_id": data["turma_id"]
    }
    alunos.append(novo)
    return jsonify(novo), 201

def get_alunos():
    return jsonify(alunos)

def get_aluno_by_id(aluno_id):
    for a in alunos:
        if a["id"] == aluno_id:
            return jsonify(a)
    return jsonify({"erro": "Aluno não encontrado"}), 404

def update_aluno(aluno_id):
    for a in alunos:
        if a["id"] == aluno_id:
            data = request.get_json()
            a["nome"] = data.get("nome", a["nome"])
            a["turma_id"] = data.get("turma_id", a["turma_id"])
            return jsonify(a)
    return jsonify({"erro": "Aluno não encontrado"}), 404

def delete_aluno(aluno_id):
    global alunos
    alunos = [a for a in alunos if a["id"] != aluno_id]
    return jsonify({"mensagem": "Removido com sucesso"})