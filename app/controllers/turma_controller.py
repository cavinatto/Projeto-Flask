from flask import request, jsonify
from app.models.professor_model import professores
from app.models.turma_model import turmas

def add_turma():
    data = request.get_json()
    if not any(p["id"] == data["professor_id"] for p in professores):
        return jsonify({"erro": "Professor não encontrado"}), 400
    nova = {
        "id": len(turmas) + 1,
        "nome": data["nome"],
        "professor_id": data["professor_id"]
    }
    turmas.append(nova)
    return jsonify(nova), 201

def get_turmas():
    return jsonify(turmas)

def get_turma_by_id(turma_id):
    for t in turmas:
        if t["id"] == turma_id:
            return jsonify(t)
    return jsonify({"erro": "Turma não encontrada"}), 404

def update_turma(turma_id):
    for t in turmas:
        if t["id"] == turma_id:
            data = request.get_json()
            t["nome"] = data.get("nome", t["nome"])
            t["professor_id"] = data.get("professor_id", t["professor_id"])
            return jsonify(t)
    return jsonify({"erro": "Turma não encontrada"}), 404

def delete_turma(turma_id):
    global turmas
    turmas = [t for t in turmas if t["id"] != turma_id]
    return jsonify({"mensagem": "Removida com sucesso"})