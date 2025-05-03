from config import app, db
from alunos.alunos_routes import alunos_blueprint
from professores.professores_routes import professores_blueprint
from turmas.turmas_routes import turmas_blueprint
from swagger.swagger_config import configure_swagger

from flask import jsonify

# Registra os blueprints
app.register_blueprint(alunos_blueprint, url_prefix='/api')
app.register_blueprint(professores_blueprint, url_prefix='/api')
app.register_blueprint(turmas_blueprint, url_prefix='/api')

# Configura Swagger
configure_swagger(app)

# Cria tabelas, se necessário
with app.app_context():
    db.create_all()

# Ponto de entrada principal
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("DEBUG", "True") == "True"
    
    app.run(host='0.0.0.0', port=port, debug=debug)
