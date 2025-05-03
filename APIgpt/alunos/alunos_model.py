from datetime import datetime, date
from config import db

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)
    turma = db.relationship("Turma", back_populates="alunos")

    def __init__(self, nome, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, turma_id):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = (nota_primeiro_semestre + nota_segundo_semestre) / 2
        self.turma_id = turma_id
        self.idade = self.calcular_idade()

    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "data_nascimento": self.data_nascimento.isoformat(),
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.media_final,
            "turma_id": self.turma_id
        }

class AlunoNaoEncontrado(Exception):
    pass

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno não encontrado.')
    return aluno.to_dict()

def adicionar_aluno(novos_dados):
    from turmas.turmas_model import Turma
    turma = Turma.query.get(novos_dados['turma_id'])
    if turma is None:
        return {"message": "Turma não existe"}, 404
    
    try:
        data_nascimento = datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date()
        nota_1 = float(novos_dados['nota_primeiro_semestre'])
        nota_2 = float(novos_dados['nota_segundo_semestre'])
    except Exception as e:
        return {"message": "Dados inválidos: " + str(e)}, 400

    novo_aluno = Aluno(
        nome=novos_dados['nome'],
        data_nascimento=data_nascimento,
        nota_primeiro_semestre=nota_1,
        nota_segundo_semestre=nota_2,
        turma_id=int(novos_dados['turma_id'])
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return {"message": "Aluno adicionado com sucesso!"}, 201

def atualizar_aluno(id_aluno, novos_dados):
    from turmas.turmas_model import Turma

    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno não encontrado.')

    aluno.nome = novos_dados.get('nome', aluno.nome)
    if 'data_nascimento' in novos_dados:
        aluno.data_nascimento = datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date()
        aluno.idade = aluno.calcular_idade()

    if 'nota_primeiro_semestre' in novos_dados:
        aluno.nota_primeiro_semestre = float(novos_dados['nota_primeiro_semestre'])
    if 'nota_segundo_semestre' in novos_dados:
        aluno.nota_segundo_semestre = float(novos_dados['nota_segundo_semestre'])
    aluno.media_final = (aluno.nota_primeiro_semestre + aluno.nota_segundo_semestre) / 2

    if 'turma_id' in novos_dados:
        turma = Turma.query.get(novos_dados['turma_id'])
        if turma is None:
            return {"message": "Turma não existe"}, 404
        aluno.turma_id = int(novos_dados['turma_id'])

    db.session.commit()
    return None

def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno não encontrado.')

    db.session.delete(aluno)
    db.session.commit()