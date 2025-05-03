from config import db

class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome}

def listar_professores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def adicionar_professor(novos_dados):
    novo_professor = Professor(nome=novos_dados['nome'])
    db.session.add(novo_professor)
    db.session.commit()
    return {"message": "Professor adicionado com sucesso!"}, 201

def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise Exception("Professor não encontrado.")
    return professor.to_dict()

def atualizar_professor(id_professor, novos_dados):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise Exception("Professor não encontrado.")
    professor.nome = novos_dados['nome']
    db.session.commit()

def excluir_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise Exception("Professor não encontrado.")
    db.session.delete(professor)
    db.session.commit()
