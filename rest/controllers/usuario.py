from os import abort

from flask import request, Blueprint, jsonify, g

#flask.g : é um objeto no Flask que possui a responsabilidade de armazenar e compartilhar
# dados através do tempo de execução de uma requisição

from rest.models.model import db, auth, Usuario

app = Blueprint("usuario", __name__)

@app.route('/api/adicionar', methods=['POST'])
def new_user():
    #*args: o * é utilizado para
    #permitir que um parâmetro aceite um número não definido de
    #argumentos para sua função(parecido com a keyword params no C # )
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        return jsonify({'ta faltando algum campo !': ''}), 400   # missing arguments
    if Usuario.query.filter_by(username=username).first() is not None:
        return jsonify({'usuario ja existe!': username}), 400   # existing user
    user = Usuario(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201

@app.route('/api/buscar/<int:id>')
def get_user(id):
    user = Usuario.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/api/gerartoken')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})

