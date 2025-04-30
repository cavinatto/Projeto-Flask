alunos = []

def criar_aluno(data):
    novo = {
        "id": len(alunos) + 1,
        "nome": data["nome"],
        "turma_id": data["turma_id"]
    }
    alunos.append(novo)
    return novo

def listar_alunos():
    return alunos

def buscar_aluno_por_id(aluno_id):
    return next((a for a in alunos if a["id"] == aluno_id), None)

def atualizar_aluno(aluno_id, data):
    aluno = buscar_aluno_por_id(aluno_id)
    if aluno:
        aluno["nome"] = data.get("nome", aluno["nome"])
        aluno["turma_id"] = data.get("turma_id", aluno["turma_id"])
    return aluno

def deletar_aluno(aluno_id):
    global alunos
    alunos = [a for a in alunos if a["id"] != aluno_id]