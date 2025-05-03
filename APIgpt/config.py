import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = int(os.environ.get('PORT', 8000))
app.config['DEBUG'] = os.environ.get('DEBUG', 'True') == 'True'

# Banco de dados vindo do ambiente
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL",
    "mysql+pymysql://root:senha@localhost:3306/escola_db"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
