class AlunoModel:
    alunos = []

    @classmethod
    def adicionar(cls, nome, turma_id):
        aluno = {"id": len(cls.alunos) + 1, "nome": nome, "turma_id": turma_id}
        cls.alunos.append(aluno)
        return aluno

    @classmethod
    def listar(cls):
        return cls.alunos

    @classmethod
    def buscar_por_id(cls, aluno_id):
        return next((a for a in cls.alunos if a["id"] == aluno_id), None)

    @classmethod
    def atualizar(cls, aluno_id, nome, turma_id):
        aluno = cls.buscar_por_id(aluno_id)
        if aluno:
            aluno["nome"] = nome
            aluno["turma_id"] = turma_id
        return aluno

    @classmethod
    def remover(cls, aluno_id):
        cls.alunos = [a for a in cls.alunos if a["id"] != aluno_id]
