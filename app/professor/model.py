from ..extensions import db

class Professor(db.Model):
    __tablename__           = 'professor'
    id                      = db.Column(db.Integer, primary_key=True)
    nome                    = db.Column(db.String(63), nullable=False)
    cpf                     = db.Column(db.String(11), nullable=False)  # SEM PONTOS OU TRAÇOS
    formacao                = db.Column(db.String(63), nullable=False)

    turmas                  = db.relationship("Turma", backref="professor")



'''

    def json(self):
        return{
            'nome': self.nome,
            'peso': self.cpf
            (...)
        }
'''