from flask import Blueprint, request, jsonify
from .alunos_model import (
    AlunoNaoEncontrado,
    listar_alunos,
    aluno_por_id,
    adicionar_aluno,
    atualizar_aluno,
    excluir_aluno
)

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = listar_alunos()
    return jsonify(alunos)

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    response, status_code = adicionar_aluno(data)
    return jsonify(response), status_code

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_aluno(id_aluno):
    data = request.json
    try:
        aluno = aluno_por_id(id_aluno)
        if not aluno:
            return jsonify({'message': 'Aluno não encontrado'}), 404

        update_response = atualizar_aluno(id_aluno, data)
        if isinstance(update_response, tuple):  # error tuple
            return jsonify(update_response[0]), update_response[1]
        return jsonify(data), 200
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return jsonify({'message': 'Aluno excluído com sucesso'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404