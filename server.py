from flask import Flask, redirect, render_template, request
from usuario import Usuario

app = Flask(__name__)

@app.route('/')
def Inicio():
    return redirect('/usuarios')

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.seleccionarTodo()
    return render_template("Leer.html", listaUsuarios = usuarios)

@app.route('/nuevo/usuario')
def nuevoUsuario():
    return render_template("crearUsuario.html")

@app.route('/crear/usuario', methods=['POST'])
def crearUsuario():
    dicUsuario = {'fnombre': request.form['fnombre'], 'fapellido': request.form['fapellido'], 'fcorreo': request.form['fcorreo']}
    Usuario.crearUsuario(dicUsuario)
    return redirect('/usuarios')

if __name__ == "__main__":
    app.run(debug = True)