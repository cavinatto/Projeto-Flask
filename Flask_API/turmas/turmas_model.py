class TurmaModel:
    turmas = []

    @classmethod
    def adicionar(cls, nome, professor_id):
        turma = {"id": len(cls.turmas) + 1, "nome": nome, "professor_id": professor_id}
        cls.turmas.append(turma)
        return turma

    @classmethod
    def listar(cls):
        return cls.turmas

    @classmethod
    def buscar_por_id(cls, id):
        return next((t for t in cls.turmas if t["id"] == id), None)

    @classmethod
    def atualizar(cls, id, nome, professor_id):
        turma = cls.buscar_por_id(id)
        if turma:
            turma["nome"] = nome
            turma["professor_id"] = professor_id
        return turma

    @classmethod
    def remover(cls, id):
        cls.turmas = [t for t in cls.turmas if t["id"] != id]
