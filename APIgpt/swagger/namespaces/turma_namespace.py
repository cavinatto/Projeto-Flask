from flask_restx import Namespace, Resource, fields
from turmas.turmas_model import listar_turmas, adicionar_turma, turma_por_id, atualizar_turma, excluir_turma

turmas_ns = Namespace("turmas", description="Operações relacionadas às turmas")

turma_model = turmas_ns.model("Turma", {
    "nome": fields.String(required=True, description="Nome da turma"),
    "professor_id": fields.Integer(required=True, description="ID do professor associado à turma"),
})

turma_output_model = turmas_ns.model("TurmaOutput", {
    "id": fields.Integer(description="ID da turma"),
    "nome": fields.String(description="Nome da turma"),
    "professor_id": fields.Integer(description="ID do professor associado à turma"),
})

@turmas_ns.route("/")
class TurmasResource(Resource):
    @turmas_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todas as turmas"""
        return listar_turmas()

    @turmas_ns.expect(turma_model)
    def post(self):
        """Cria uma nova turma"""
        data = turmas_ns.payload
        response, status_code = adicionar_turma(data)
        return response, status_code

@turmas_ns.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_with(turma_output_model)
    def get(self, id_turma):
        """Obtém uma turma pelo ID"""
        return turma_por_id(id_turma)

    @turmas_ns.expect(turma_model)
    def put(self, id_turma):
        """Atualiza uma turma pelo ID"""
        data = turmas_ns.payload
        atualizar_turma(id_turma, data)
        return data, 200

    def delete(self, id_turma):
        """Exclui uma turma pelo ID"""
        excluir_turma(id_turma)
        return {"message": "Turma excluída com sucesso"}, 200
