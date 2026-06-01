from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)

app.secret_key = "fsc"

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="notas"
    )

@app.route("/")
@app.route("/inicio")

def inicio():

    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])

def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        conexao = conectar()

        cursor = conexao.cursor()

        sql = """
        SELECT *
        FROM usuarios
        WHERE usuario = %s AND senha = %s
        """

        cursor.execute(sql, (usuario, senha))

        resultado = cursor.fetchone()

        conexao.close()

        if resultado:

            session["usuario"] = resultado[1]
            session["id_usuario"] = resultado[0]

            return redirect("/aluno")

        else:

            return render_template(
                "index.html",
                erro="Usuário ou senha inválidos"
            )

    return render_template("login.html")

@app.route("/contato")

def contato():

    return render_template("contato.html")

@app.route("/aluno")

def aluno():

    if "usuario" not in session:

        return redirect("/login")

    id_usuario = session["id_usuario"]

    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
    SELECT materia, nota, faltas
    FROM notas_alunos
    WHERE usuario_id = %s
    """

    cursor.execute(sql, (id_usuario,))

    notas = cursor.fetchall()

    conexao.close()

    return render_template(
        "aluno.html",
        notas=notas
    )

@app.route("/logout")

def logout():

    session.clear()

    return redirect("/inicio")

if __name__ == "__main__":

    app.run(debug=True)