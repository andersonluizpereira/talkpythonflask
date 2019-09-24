from flask import Flask


from rest.controllers.estudante import app as estudante_controller
from rest.controllers.disciplina import app as disciplina_controller
from rest.controllers.usuario import app as usuario_controller
from rest.models.model import db

app = Flask(__name__, template_folder='templates')

#SQLite é um pacote que disponibiliza um Sistema Gerenciador de Banco de Dados Relacional e
# permite ser executado através de linha de comando, possibilitando executar qualquer
# query SQL básica de maneira simples. (Nossa aplicação não dependerá desse pacote para ser executada,
# mas seria bom já instalá-lo caso surja a necessidade de executar alguma query SQL no banco)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.register_blueprint(estudante_controller, url_prefix="/estudante/")
app.register_blueprint(disciplina_controller, url_prefix="/disciplina/")
app.register_blueprint(usuario_controller, url_prefix="/usuario/")

#Blueprint basicamente permite que um módulo estenda a aplicação principal e
# funcione similarmente a aplicação Flask. Sendo esta uma das grandes vantagem para aplicações maiores,
# por permitir a modularização de uma aplicação, o que facilita em muito a organização,
# desenvolvimento e manutenções do código fonte.

@app.route("/")
def index():
    return "Index"

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run()