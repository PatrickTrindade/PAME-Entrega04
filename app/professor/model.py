from ..extensions import db

class Professor(db.Model):
    __tablename__           = 'professor'
    id                      = db.Column(db.Integer, primary_key=True)
    nome                    = db.Column(db.String(63), nullable=False)
    cpf                     = db.Column(db.String(11), nullable=False)  # SEM PONTOS OU TRAÇOS
    formação                = db.Column(db.String(63), nullable=False)

    turmas                  = db.relationship("Turma", backref="professor")



'''
    trofeu = db.relationship('Trofeu', backref='lutador_id') #era backref='owner'

    association = db.relationship('Torneio', secondary=association_table, backref='lutador')



    def json(self):
        return{
            'nome': self.nome,
            'peso': self.peso
        }
'''