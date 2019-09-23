#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/operacoesint/')
@app.route('/operacoesint/<int:num1>/<int:num2>')
def escrevanatelaoperacoesint(num1=1,num2=2):
    soma = 1

    soma = soma + 1
    # Outra forma
    soma += 1

    subtracao = 1

    subtracao = subtracao - 1
    # Outra forma
    subtracao -= 1
    return "<h1>Números num1: {}, num2: {}</h1> <br/>" \
           "<h1>Soma {}</h1> <br/> " \
           "<h1>Subtracao {}</h1> <br/> " \
           "<br/>".format(num1,num2,soma, subtracao)

@app.route('/operacoesf/')
@app.route('/operacoesf/<float:num1>/<float:num2>')
def escrevanatelaoperacoesf(num1=7.8,num2=8.3):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    modulo = num1 % num2
    return "<h1>Números num1: {}, num2: {}</h1> <br/>" \
           "<h1>Soma {}</h1> <br/> " \
           "<h1>Subtracao {}</h1> <br/> " \
           "<h1>Multiplicacao {}</h1> <br/> " \
           "<h1>Divisao {}</h1> <br/>" \
           "<h1>Modulo, resto da divisao {}</h1> " \
           "<h1>Flutuante {}</h1> " \
           "<br/>".format(num1,num2,soma, subtracao, multiplicacao, divisao, modulo,num1)

@app.route('/operacoes/')
@app.route('/operacoes/<int:num1>/<int:num2>')
#Você pode adicionar seções variáveis a um URL marcando seções com <nome da variável>.
# Sua função então recebe o <nome da variável> como um argumento de palavra-chave.
# Opcionalmente, você pode usar um conversor para especificar o tipo de argumento como <converter: variable_name>.
def escrevanatelaoperacoes(num1=10,num2=10):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    modulo = num1 % num2
    return "<h1>Números num1: {}, num2: {}</h1> <br/>" \
           "<h1>Soma {}</h1> <br/> " \
           "<h1>Subtracao {}</h1> <br/> " \
           "<h1>Multiplicacao {}</h1> <br/> " \
           "<h1>Divisao {}</h1> <br/>" \
           "<h1>Modulo, resto da divisao {}</h1> " \
           "<br/>".format(num1,num2,soma, subtracao, multiplicacao, divisao, modulo)


if __name__ == '__main__':
    app.run(debug=True)