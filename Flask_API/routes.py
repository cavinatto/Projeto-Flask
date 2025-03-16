from flask import Blueprint, jsonify, request

bp = Blueprint('routes', __name__)

# Listas de Armazenamento
professores = []
turmas = []
alunos = []

# CRUD Professores
@bp.route('/professores', methods=['POST'])
def add_professor():
    data = request.json
    novo_professor = {"id": len(professores) + 1, "nome": data["nome"]}
    professores.append(novo_professor)
    return jsonify(novo_professor), 201

@bp.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(professores)

@bp.route('/professores/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    data = request.json
    for professor in professores:
        if professor["id"] == professor_id:
            professor["nome"] = data["nome"]
            return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@bp.route('/professores/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    global professores
    professores = [p for p in professores if p["id"] != professor_id]
    return jsonify({"mensagem": "Professor removido com sucesso"}), 200

# CRUD Turmas
@bp.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(turmas)

@bp.route('/turmas', methods=['POST'])
def add_turma():
    data = request.json
    nova_turma = {"id": len(turmas) + 1, "nome": data["nome"], "professor_id": data["professor_id"]}
    turmas.append(nova_turma)
    return jsonify(nova_turma), 201

@bp.route('/turmas/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    data = request.json
    for turma in turmas:
        if turma["id"] == turma_id:
            turma["nome"] = data["nome"]
            turma["professor_id"] = data["professor_id"]
            return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@bp.route('/turmas/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    global turmas
    turmas = [t for t in turmas if t["id"] != turma_id]
    return jsonify({"mensagem": "Turma removida com sucesso"}), 200

# CRUD Alunos
@bp.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

@bp.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.json
    novo_aluno = {"id": len(alunos) + 1, "nome": data["nome"], "turma_id": data["turma_id"]}
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

@bp.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    data = request.json
    for aluno in alunos:
        if aluno["id"] == aluno_id:
            aluno["nome"] = data["nome"]
            aluno["turma_id"] = data["turma_id"]
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    global alunos
    alunos = [a for a in alunos if a["id"] != aluno_id]
    return jsonify({"mensagem": "Aluno removido com sucesso"}), 200
