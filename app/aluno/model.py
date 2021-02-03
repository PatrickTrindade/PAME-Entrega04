from ..extensions import db
from ..association import association_table

class Aluno(db.Model):
    __tablename__           = 'aluno'
    id                      = db.Column(db.Integer, primary_key=True)
    nome                    = db.Column(db.String(63), nullable=False)
    cpf                     = db.Column(db.String(11), nullable=False)  # SEM PONTOS OU TRAÇOS
    data_de_nascimento      = db.Column(db.String(10), nullable=False)
    sexo                    = db.Column(db.String(10), nullable=False)
    periodo_de_ingresso     = db.Column(db.String(4), nullable=False)
    curso                   = db.Column(db.String(63), nullable=False)

    boletim_id              = db.Column(db.Integer, ForeignKey('boletim.id')) 
    boletim                 = db.relationship('Boletim', backref='aluno')

    turma                   = db.relationship('Turma', secondary=association_table, backref='aluno')


    
'''
    association = db.relationship('Lutadores', secondary=association_table, backref='torneio')
'''