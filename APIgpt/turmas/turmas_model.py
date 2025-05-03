from config import db

class Turma(db.Model):
    __tablename__ = "turmas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey("professores.id"), nullable=False)
    alunos = db.relationship("Aluno", back_populates="turma")

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'professor_id': self.professor_id
        }

def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def adicionar_turma(novos_dados):
    nova_turma = Turma(nome=novos_dados['nome'], professor_id=novos_dados['professor_id'])
    db.session.add(nova_turma)
    db.session.commit()
    return {"message": "Turma adicionada com sucesso!"}, 201

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise Exception("Turma não encontrada.")
    return turma.to_dict()

def atualizar_turma(id_turma, novos_dados):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise Exception("Turma não encontrada.")
    turma.nome = novos_dados['nome']
    turma.professor_id = novos_dados['professor_id']
    db.session.commit()

def excluir_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise Exception("Turma não encontrada.")
    db.session.delete(turma)
    db.session.commit()
