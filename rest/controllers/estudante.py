from flask import request, Blueprint, Response

import json

from rest.models.model import auth, Estudante, db

app = Blueprint("estudante", __name__)

@app.route("/api/listar")
@auth.login_required
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route("/api/estudantes", methods=["GET"])
@app.route("/api/estudantes/<int:limit>", methods=["GET"])
@auth.login_required
def lista(limit=1):
    rows = db.session.execute("select id,nome,idade from Estudante limit "+str(limit)+"").fetchall()
    result = [dict(r) for r in rows]
    print(json.dumps(result))
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route("/api/buscar/<int:id>", methods=["GET"])
@auth.login_required
def view(id):
    row = db.session.execute("select id,nome,idade from Estudante where id= %s" %id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")

@app.route("/api/adicionar", methods=["POST"])
@auth.login_required
def add():
    estudante = Estudante(request.form['nome'], request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return Response(response=json.dumps({'status':'success','data':estudante.to_dict()}), status=200, content_type="application/json")

@app.route("/api/excluir/<int:id>", methods=["DELETE"])
@auth.login_required
def delete(id):
    estudante = Estudante.query.get(id)
    if estudante:
        db.session.delete(estudante)
        db.session.commit()
        return Response(response=json.dumps(estudante.to_dict()), status=202, content_type="application/json")
    return Response(response=json.dumps({'message':'estudante não existe!'}), status=200, content_type="application/json")

@app.route("/api/editar/<int:id>", methods=["PUT","POST"])
@auth.login_required
def edit(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=202, content_type="application/json")