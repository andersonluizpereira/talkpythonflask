#SQLAlchemy é uma poderosa ferramenta ORM que possibilita aos desenvolvedores
# trabalhar com dados armazenados no banco de dados de maneira flexível e simplificada.
from flask_sqlalchemy import SQLAlchemy
#Biblioteca que permite autenticacao Autorizathion: Basic
from flask_httpauth import HTTPBasicAuth

#O PassLib fornece vários algoritmos de hash para você escolher.
# O objeto custom_app_context é uma opção fácil de usar, com base no algoritmo de hash sha256_crypt.
from passlib.apps import custom_app_context as pwd_context

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
#https://stackoverflow.com/questions/15083967/when-should-flask-g-be-used
from flask import g

db = SQLAlchemy()
auth = HTTPBasicAuth()

class Estudante(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "nome":self.nome, "idade":self.idade}
        else:
            return { col: getattr(self, col) for col in columns}

class Disciplina(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "nome": self.nome}
        else:
            return {col: getattr(self, col) for col in columns}


class Usuario(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer('the quick brown fox jumps over the lazy dog', expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('the quick brown fox jumps over the lazy dog')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = Usuario.query.get(data['id'])
        return user


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = Usuario.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = Usuario.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
