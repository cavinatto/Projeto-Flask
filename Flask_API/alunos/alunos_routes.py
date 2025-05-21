from flask import Blueprint, request, jsonify
from alunos.alunos_model import AlunoModel
from turmas.turmas_model import TurmaModel

bp = Blueprint('alunos', __name__, url_prefix='/alunos')

@bp.route('', methods=['POST'])
def criar():
    dados = request.get_json()
    if not TurmaModel.buscar_por_id(dados['turma_id']):
        return jsonify({"erro": "turma nao encontrada"}), 400
    aluno = AlunoModel.adicionar(dados['nome'], dados['turma_id'])
    return jsonify(aluno), 201

@bp.route('', methods=['GET'])
def listar():
    return jsonify(AlunoModel.listar())

@bp.route('/<int:aluno_id>', methods=['GET'])
def buscar(aluno_id):
    aluno = AlunoModel.buscar_por_id(aluno_id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@bp.route('/<int:aluno_id>', methods=['PUT'])
def atualizar(aluno_id):
    dados = request.get_json()
    aluno = AlunoModel.atualizar(aluno_id, dados['nome'], dados['turma_id'])
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@bp.route('/<int:aluno_id>', methods=['DELETE'])
def deletar(aluno_id):
    AlunoModel.remover(aluno_id)
    return jsonify({"mensagem": "Aluno removido com sucesso"})
