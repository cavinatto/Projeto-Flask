professores = []

def criar_professor(data):
    novo = {"id": len(professores) + 1, "nome": data["nome"]}
    professores.append(novo)
    return novo

def listar_professores():
    return professores

def buscar_professor_por_id(professor_id):
    return next((p for p in professores if p["id"] == professor_id), None)

def atualizar_professor(professor_id, data):
    prof = buscar_professor_por_id(professor_id)
    if prof:
        prof["nome"] = data.get("nome", prof["nome"])
    return prof

def deletar_professor(professor_id):
    global professores
    professores = [p for p in professores if p["id"] != professor_id]