from flask import Blueprint
from app.routes.aluno_routes import aluno_bp
from app.routes.professor_routes import professor_bp
from app.routes.turma_routes import turma_bp

bp = Blueprint('routes', __name__)

bp.register_blueprint(aluno_bp)
bp.register_blueprint(professor_bp)
bp.register_blueprint(turma_bp)
