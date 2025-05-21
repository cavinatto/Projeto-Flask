from flask import Flask
from alunos.alunos_routes import bp as alunos_bp
from professores.professores_routes import bp as professores_bp
from turmas.turmas_routes import bp as turmas_bp

app = Flask(__name__)

app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)

if __name__ == '__main__':
    app.run(debug=True)
