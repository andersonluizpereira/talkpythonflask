#!flask/bin/python
from flask import Flask,jsonify,render_template

app = Flask(__name__, template_folder='template')


@app.route("/index", methods=['GET'])
def indexhtml():
   nome = "Anderson"
   posts = ["Flask Basico","Flask Intermediario","Flask Avancado"]
   return render_template("index.html",nome=nome,posts=posts)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message":"Hello World!"})

if __name__ == '__main__':
    app.run(debug=True,port=8080)