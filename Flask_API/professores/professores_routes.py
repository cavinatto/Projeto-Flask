from flask import Blueprint, request, jsonify
from professores.professores_model import ProfessorModel

bp = Blueprint('professores', __name__, url_prefix='/professores')

@bp.route('', methods=['POST'])
def criar():
    dados = request.get_json()
    prof = ProfessorModel.adicionar(dados['nome'])
    return jsonify(prof), 201

@bp.route('', methods=['GET'])
def listar():
    return jsonify(ProfessorModel.listar())

@bp.route('/<int:id>', methods=['GET'])
def buscar(id):
    prof = ProfessorModel.buscar_por_id(id)
    if prof:
        return jsonify(prof)
    return jsonify({"erro": "professor nao encontrado"}), 404

@bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    prof = ProfessorModel.atualizar(id, dados['nome'])
    if prof:
        return jsonify(prof)
    return jsonify({"erro": "professor nao encontrado"}), 404

@bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    ProfessorModel.remover(id)
    return jsonify({"mensagem": "Professor removido com sucesso"})
