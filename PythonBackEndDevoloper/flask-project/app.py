from flask import Flask

app = Flask(__name__)

valor = "dinâmica"


@app.route("/")
def hello_world():
    return """<p>Hello, World!</p>"""
