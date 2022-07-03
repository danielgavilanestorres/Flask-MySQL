import re
from flask import Flask, redirect, render_template, request
from usuario import Usuario

app = Flask(__name__)

@app.route('/')
def Inicio():
    print("Inicio")
    return redirect('/usuarios')

@app.route('/usuarios')
def usuarios():
    listaUsuarios = Usuario.mostrarTodo()
    return render_template("usuarios.html", listaUsuarios = listaUsuarios)

@app.route('/nuevo/usuario')
def nuevoUsuario():
    return render_template("crudUsuarios.html")

@app.route('/crearUsuario', methods = ['post'])
def crearUsuario():
    dicUsuario = {'fnombre': request.form['fnombre'], 'fapellido': request.form['fapellido'], 'fcorreo': request.form['fcorreo']}
    id = Usuario.crearUsuario(dicUsuario)
    return redirect('/mostrar/usuario/' + str(id))

@app.route('/mostrar/usuario/<int:id>')
def mostrarUsuarioId(id):
    dicId = {'id': id}
    usuario = Usuario.mostrarUsuarioId(dicId)
    return render_template("verUsuario.html", usuario = usuario)

@app.route('/editar/usuario/<int:id>')
def editarUsuarioEdit(id):
    dicId = {'id': id}
    usuario = Usuario.mostrarUsuarioId(dicId)
    return render_template("editarUsuario.html", usuario = usuario)

@app.route('/guardar/usuario/<int:id>', methods = ['post'])
def guardarUsuarioEdit(id):
    dicUsuario = {'id': id, 'fnombre': request.form['fnombre'], 'fapellido': request.form['fapellido'], 'fcorreo': request.form['fcorreo']}
    Usuario.actualizarUsuario(dicUsuario)
    return redirect('/mostrar/usuario/' + str(id))

@app.route('/eliminar/usuario/<int:id>')
def eliminarUsuario(id):
    dicId = {'id': id}
    Usuario.eliminarUsuario(dicId)
    return redirect('/usuarios')

if __name__ == "__main__":
    app.run(debug = True)