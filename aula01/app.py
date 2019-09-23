#!flask/bin/python
from flask import Flask,jsonify,render_template

#render_template: passando o nome do modelo e a variáveis ele vai renderizar o template


#Nessa linha é instanciado um objeto da classe Flask, é ele que vamos utilizar para configurar a nossa aplicação
# e para executa-la com o servidor de testes do próprio Flask.
#Caso queira configurar uma pasta criar aplicações web, utilize a nomenclatura template_folder
app = Flask(__name__, template_folder='template')


@app.route("/index", methods=['GET'])
def indexhtml():
   nome = "Anderson"
   posts = ["Flask Basico","Flask Intermediario","Flask Avancado"]
   return render_template("index.html",nome=nome,posts=posts)

#@app.route("/") - É um decorator responsável por interpretar a rota que acessamos,
# então, assim que é acessada a url / como é configurado na linha acima,
#a função que está abaixo é responsável por enviar uma rota ao navegador.
@app.route('/', methods=['GET'])
def index():
   # A função jsonify() no flask retorna
   #um objeto flask.Response() que já possui o
   #cabeçalho de tipo de conteúdo apropriado 'application / json'
   #para uso com respostas json.Considerando que, o método json.dumps() retornará apenas uma cadeia codificada, o que exigiria adicionar manualmente o cabeçalho do tipo MIME.
    return jsonify({"message":"Hello World!"})

# app.run(debug=True) → essas instruções definem que quando o "app.py" for executado via linha de comando.
# O Flask deverá iniciar o seu servidor interno para executar a aplicação,
# como no construtor foi passado o valor "True" para a chave "debug",
# o servidor será iniciado no modo debug; assim, quando forem feitas modificações no código e elas
# forem salvas o servidor irá reiniciar automaticamente para que você possa testar o novo código.
if __name__ == '__main__':
    # Porta padrão - 5000 → é a porta padrão do Flask, você pode mudá-la passando o parâmetro "port no contrutor",
    # deixando ele da seguinte forma:
    #Obs: Debug não deve ser utilizado em ambiente de produção!
    app.run(debug=True,port=8080)
