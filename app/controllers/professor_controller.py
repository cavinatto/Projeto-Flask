from flask import request, jsonify
from app.models.professor_model import professores

def add_professor():
    data = request.get_json()
    novo = {"id": len(professores) + 1, "nome": data["nome"]}
    professores.append(novo)
    return jsonify(novo), 201

def get_professores():
    return jsonify(professores)

def get_professor_by_id(professor_id):
    for prof in professores:
        if prof["id"] == professor_id:
            return jsonify(prof)
    return jsonify({"erro": "Professor não encontrado"}), 404

def update_professor(professor_id):
    for prof in professores:
        if prof["id"] == professor_id:
            data = request.get_json()
            prof["nome"] = data.get("nome", prof["nome"])
            return jsonify(prof)
    return jsonify({"erro": "Professor não encontrado"}), 404

def delete_professor(professor_id):
    global professores
    professores = [p for p in professores if p["id"] != professor_id]
    return jsonify({"mensagem": "Removido com sucesso"})