from flask import Flask
from .config import Config
from .extensions import db

from .aluno.model import Aluno
from .boletim.model import Boletim
from .materia.model import Materia
from .professor.model import Professor
from .turma.model import Turma

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    return app