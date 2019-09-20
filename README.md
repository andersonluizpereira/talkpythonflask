

#Instalar essas duas dependencias
#pip install flask
#pip install Jinja2

#Ler https://restfulapi.net/http-status-codes/
#Ler https://www.eximiaco.tech/pt/2019/09/13/origem-e-significado-de-rest-e-restful/


#Você pode jogar esse código em um arquivo chamado "run.py", esse será o arquivo principal da sua aplicação em Flask, pois é ele que vamos executar e será responsável por chamar os próximos.

#Entendendo um pouco do código:

#app = Flask(__name__) → nessa linha é instanciado um objeto da classe Flask, é ele que vamos utilizar para configurar a nossa aplicação e para executa-la com o servidor de testes do próprio Flask.

#@app.route("/") → é um decorator responsável por interpretar a rota que acessamos, então, assim que é acessada a url / como é configurado na linha acima, a função que está abaixo é responsável por enviar uma rota ao navegador.

#def index():
#    return "Hello Flask!" → é a função que tem como objetivo retornar somente um texto plano como Hello Flask.

#if __name__ == '__main__':
#    app.run(debug=True) → essas instruções definem que quando o "run.py" for executado via linha de comando. O Flask deverá iniciar o seu servidor interno para executar a aplicação, como no construtor foi passado o valor "True" para a chave "debug", o servidor será iniciado no modo debug; assim, quando forem feitas modificações no código e elas forem salvas o servidor irá reiniciar automaticamente para que você possa testar o novo código.

#Esse é o código mais básico que se pode ter em Flask.

#Para acessar a sua aplicação, você pode acessar o endereço: http://localhost:5000

#5000 → é a porta padrão do Flask, você pode mudá-la passando o parâmetro "port no contrutor", deixando ele da seguinte forma:

#if __name__ == '__main__':
#    app.run(debug=True,port=6543)
