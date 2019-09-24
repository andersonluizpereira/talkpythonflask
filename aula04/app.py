#!flask/bin/python
from flask import Flask
app = Flask(__name__)


from flask import Flask, redirect, url_for

app = Flask(__name__)

#URL Building
#Para criar um URL para uma função específica,
# use a função url_for ().
# Ele aceita o nome da função como seu primeiro argumento e qualquer número de argumentos de palavras-chave,
# cada um correspondendo a uma parte variável da regra de URL.
# Partes variáveis desconhecidas são anexadas ao URL como parâmetros de consulta.

@app.route("/admin")
def admin():
    return "<h1>Admin</h1>"

@app.route("/guest/<guest>")
def guest(guest):
    return "<p>Olá guest <b>%s</b></p>" %guest

@app.route("/user/<name>")
def user(name=""):
    if name == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))

@app.route("/google")
def google():
    return redirect("http://google.com")

if __name__ == '__main__':
    app.run(debug=True)
