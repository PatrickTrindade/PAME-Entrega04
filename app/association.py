from .extensions import db

association_table = db.Table('association', db.Model.metadata,                                  #(?) db.Table('$nome-da-tabela')
                            db.Column('aluno', db.Integer, db.ForeignKey('aluno.id')),      #(?) db.Column()
                            db.Column('turma', db.Integer, db.ForeignKey('turma.id')) 
                            
