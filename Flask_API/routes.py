from flask import Blueprint, jsonify, request

bp = Blueprint('routes',__name__)

professores = []
turmas = []
alunos = []

# Lista de Professores - CREATE
@bp.route('/professores', methods=['POST'])
def add_professores():  
    data = request.json
    novo_professor = {"id": len(professores) + 1, "nome": data["nome"]}
    professores.append(novo_professor)
    return jsonify(novo_professor), 201

# READ
@bp.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(professores)

# UPDATE
bp.route('/professores/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
        data = request.json
        for professor in professores:
            if professor["id"] == professor_id:
                 professor["nome"] = data["nome"]
                 return jsonify(professor)
        return jsonify({"erro": "Professor não encontrado"}), 404                    
