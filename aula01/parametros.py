#!flask/bin/python
from flask import Flask,jsonify,render_template

app = Flask(__name__, template_folder='template')

@app.route('/operacoes/', methods=['GET'])
@app.route('/operacoes/<int:num1>/<int:num2>', methods=['GET','POST'])
@app.route('/operacoes/<float:num1>/<float:num2>', methods=['GET','POST'])
def escrevanatelaoperacoes(num1=10,num2=10):
    print
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    modulo = num1 % num2
    return "<h1>Números num1: {}, num2: {}</h1> " \
           "<br/><h1>Soma {}</h1> <br/> <h1>Subtracao {}</h1> " \
           "<br/> <h1>Multiplicacao {}</h1> <br/> <h1>Divisao {}</h1> " \
           "<br/><h1>Modulo, resto da divisao {}</h1> " \
           "<br/>".format(num1,num2,soma, subtracao, multiplicacao, divisao, modulo)


@app.route('/print/')
@app.route('/print/<nome>', methods=['GET'])
def escrevanatelaseunome(nome=""):
    return "<h1>Hello {}</h1>".format(nome)

if __name__ == '__main__':
    app.run(debug=True,port=6543)