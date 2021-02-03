from ..extensions import db

class Materia(db.Model):
    __tablename__           = 'materia'
    id                      = db.Column(db.Integer, primary_key=True)
    nome                    = db.Column(db.String(63), nullable=False)
    codigo                  = db.Column(db.String(63), nullable=False)

    turmas                  = db.relationship("Turma", backref="materia")

'''
    def json():
        return {
            'owner': 
        }
'''