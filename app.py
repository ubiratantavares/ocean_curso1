from flask import Flask, render_template

app = Flask("Ola")

@app.route("/")
def ola():
    return "Olá mundo! Bom dia."

@app.route("/alunos")
def aluno():
    return render_template("hello.html")

