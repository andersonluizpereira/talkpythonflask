from flask import Flask


from rest.controllers.estudante import app as estudante_controller
from rest.controllers.disciplina import app as disciplina_controller
from rest.controllers.usuario import app as usuario_controller
from rest.models.model import db

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.register_blueprint(estudante_controller, url_prefix="/estudante/")
app.register_blueprint(disciplina_controller, url_prefix="/disciplina/")
app.register_blueprint(usuario_controller, url_prefix="/usuario/")

@app.route("/")
def index():
    return "Index"

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run()