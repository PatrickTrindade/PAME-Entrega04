from ..extensions import db

class Boletim(db.Model):
    __tablename__           = 'boletim'
    id                      = db.Column(db.Integer, primary_key=True)
    nome                    = db.Column(db.String(63), nullable=False)
    codigo                  = db.Column(db.String(63), nullable=False)

    aluno_id                = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    aluno                   = db.relationship('Aluno', backref='boletim')


'''
    def json():
        return {
            'key': 
        }
'''