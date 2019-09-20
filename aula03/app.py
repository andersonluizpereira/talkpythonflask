#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/lista/<nome>')
def add(nome):
    lista = {"alface", "tomate", "cenoura", "beterraba"}
    lista.add(nome)
    return "Lista, obs:tente adicionar o mesmo que não é repetido {}".format(lista)



@app.route('/')
def index():
    lista = ["alface", "tomate", "cenoura"]
    lista1 = ["alface", "tomate", "cenoura"]
    lista.sort()
    return "Lista normal {},ordernada {}".format(lista1,lista)

if __name__ == '__main__':
    app.run(debug=True)