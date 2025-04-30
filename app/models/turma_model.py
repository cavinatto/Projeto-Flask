turmas = []
from app.models.professor_model import buscar_professor_por_id

def criar_turma(data):
    if not buscar_professor_por_id(data["professor_id"]):
        return None
    nova = {
        "id": len(turmas) + 1,
        "nome": data["nome"],
        "professor_id": data["professor_id"]
    }
    turmas.append(nova)
    return nova

def listar_turmas():
    return turmas

def buscar_turma_por_id(turma_id):
    return next((t for t in turmas if t["id"] == turma_id), None)

def atualizar_turma(turma_id, data):
    turma = buscar_turma_por_id(turma_id)
    if turma:
        turma["nome"] = data.get("nome", turma["nome"])
        turma["professor_id"] = data.get("professor_id", turma["professor_id"])
    return turma

def deletar_turma(turma_id):
    global turmas
    turmas = [t for t in turmas if t["id"] != turma_id]