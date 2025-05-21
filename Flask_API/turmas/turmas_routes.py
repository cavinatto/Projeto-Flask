from flask import Blueprint, request, jsonify
from turmas.turmas_model import TurmaModel
from professores.professores_model import ProfessorModel

bp = Blueprint('turmas', __name__, url_prefix='/turmas')

@bp.route('', methods=['POST'])
def criar():
    dados = request.get_json()
    if not ProfessorModel.buscar_por_id(dados['professor_id']):
        return jsonify({"erro": "professor nao encontrado"}), 400
    turma = TurmaModel.adicionar(dados['nome'], dados['professor_id'])
    return jsonify(turma), 201

@bp.route('', methods=['GET'])
def listar():
    return jsonify(TurmaModel.listar())

@bp.route('/<int:id>', methods=['GET'])
def buscar(id):
    turma = TurmaModel.buscar_por_id(id)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    turma = TurmaModel.atualizar(id, dados['nome'], dados['professor_id'])
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    TurmaModel.remover(id)
    return jsonify({"mensagem": "Turma removida com sucesso"})
