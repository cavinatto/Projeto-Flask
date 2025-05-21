class ProfessorModel:
    professores = []

    @classmethod
    def adicionar(cls, nome):
        professor = {"id": len(cls.professores) + 1, "nome": nome}
        cls.professores.append(professor)
        return professor

    @classmethod
    def listar(cls):
        return cls.professores

    @classmethod
    def buscar_por_id(cls, id):
        return next((p for p in cls.professores if p["id"] == id), None)

    @classmethod
    def atualizar(cls, id, nome):
        prof = cls.buscar_por_id(id)
        if prof:
            prof["nome"] = nome
        return prof

    @classmethod
    def remover(cls, id):
        cls.professores = [p for p in cls.professores if p["id"] != id]
