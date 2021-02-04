from ..extensions import db

class Boletim(db.Model):    # Considerando as alterações feitas, talvez "Notas" fosse um nome mais apropriado para esta tabela
    __tablename__           = 'boletim'
    id                      = db.Column(db.Integer, primary_key=True)
    nota                    = db.Column(db.Integer, nullable=False)

    materia_id              = db.Column(db.Integer, db.ForeignKey('materia.id'))
    materia                 = db.relationship('Materia', backref='boletim')

    aluno_id                = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    aluno                   = db.relationship('Aluno', backref='boletim')


'''
    def json():
        return {
            'key': 
        }
'''