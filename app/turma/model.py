from ..extensions import db

class Turma(db.Model):
    __tablename__           = 'turma'
    id                      = db.Column(db.Integer, primary_key=True)
    nome                    = db.Column(db.String(63), nullable=False)
    cpf                     = db.Column(db.String(11), nullable=False)  # SEM PONTOS OU TRAÇOS
    formação                = db.Column(db.String(63), nullable=False)

    professor_id            = db.Column(db.String, ForeignKey('professor.id'))
    professor               = db.relationship("Professor", backref="turmas")

    materia_id              = db.Column(db.String, ForeignKey('materia.id'))
    materia                 = db.relationship("Materia", backref="turmas")

    aluno                   = db.relationship('Aluno', secondary=association_table, backref='turma')


'''
    trofeu = db.relationship('Trofeu', backref='lutador_id') #era backref='owner'

    association = db.relationship('Torneio', secondary=association_table, backref='lutador')



    def json(self):
        return{
            'nome': self.nome,
            'peso': self.peso
        }
'''