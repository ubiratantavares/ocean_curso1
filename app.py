from flask import Flask

app = Flask("Ola")

@app.route("/")
def ola():
    return "Olá mundo! Bom dia."

@app.route("/alunos")
def aluno():
    return "João, Maria, José e Lucas"

