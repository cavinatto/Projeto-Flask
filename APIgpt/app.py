from config import app, db
from alunos.alunos_routes import alunos_blueprint
from professores.professores_routes import professores_blueprint
from turmas.turmas_routes import turmas_blueprint

from swagger.swagger_config import configure_swagger

# Registrar blueprints das rotas da api
app.register_blueprint(alunos_blueprint, url_prefix='/api')
app.register_blueprint(professores_blueprint, url_prefix='/api')
app.register_blueprint(turmas_blueprint, url_prefix='/api')

# Configurar swagger com Flask-RESTx
configure_swagger(app)

with app.app_context():
    db.create_all()

from flask import jsonify
from config import db  # Certifique-se de que você está importando o objeto db corretamente


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
