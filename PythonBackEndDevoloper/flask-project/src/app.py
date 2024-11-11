from flask import Flask, url_for, request


app = Flask(__name__)

nome = "Lucas de Souza Santos"


@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    return f"""<p>Tipo das variávies usuario, idade e altura: {type(usuario)}
          , {type(idade)}, {type(altura)}.</p>"""


@app.route("/sejabemvindo")
def seja_bem_vindo():
    return f"<p>Seja Bem-Vindo, {nome}! </p>"


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about', methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return 'This is a GET'
    else:
        return 'This is a POST'


with app.test_request_context():
    print(url_for('seja_bem_vindo'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('hello_world', usuario="lucas", idade=32, altura=1.65))
