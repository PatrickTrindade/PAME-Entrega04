from ..extensions import db
from ..association import association_table

class Turma(db.Model):
    __tablename__           = 'turma'
    id                      = db.Column(db.Integer, primary_key=True)
    horario                 = db.Column(db.String(63), nullable=False) # talvez exista o tipo timestamp

    professor_id            = db.Column(db.String, ForeignKey('professor.id'))
    professor               = db.relationship("Professor", backref="turmas")

    materia_id              = db.Column(db.String, ForeignKey('materia.id'))
    materia                 = db.relationship("Materia", backref="turmas")

    aluno                   = db.relationship('Aluno', secondary=association_table, backref='turma')


'''
    def json(self):
        return{
            'nome': self.nome,
            'peso': self.formacao
        }
'''