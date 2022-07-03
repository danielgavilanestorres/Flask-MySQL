from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.usuario import Usuario

@app.route('/')
def inicio():
    print("Inicio")
    return redirect('/usuarios')

@app.route('/usuarios')
def usuarios():
    listaUsuarios = Usuario.mostrarTodosUsuarios() 
    return render_template("mostrarUsuarios.html", listaUsuarios = listaUsuarios)

@app.route('/mostrar/usuario/<int:id>')
def mostrarUsuarioId(id):
    dicUsuario = {'id': id}
    usuario = Usuario.mostrarUnUsuario(dicUsuario)
    return render_template("mostrarUnUsuario.html", usuario = usuario)

@app.route('/nuevo/usuario')
def nuevoUsuario():
    return render_template("nuevoUsuario.html")

@app.route('/crearUsuario', methods = ['post'])
def crearUsuario():
    dicUsuario = {'fnombre': request.form['fnombre'], 'fapellido': request.form['fapellido'], 'fcorreo': request.form['fcorreo'] }
    Usuario.nuevoUsuario(dicUsuario)
    return redirect('/usuarios')
    

@app.route('/editar/usuario/<int:id>')
def verUsuarioEdit(id):
    dicUsario = {'id': id}
    usuario = Usuario.mostrarUnUsuario(dicUsario)
    return render_template("editarUsuario.html", usuario = usuario)

@app.route('/guardar/usuario/<int:id>', methods = ['post'])
def guardarUsuario(id):
    dicUsuario = {'id': id, 'fnombre':request.form['fnombre'], 'fapellido': request.form['fapellido'], 'fcorreo': request.form['fcorreo']}
    Usuario.editarUsuario(dicUsuario)
    return redirect('/mostrar/usuario/' + str(id))

@app.route('/eliminar/usuario/<int:id>')
def eliminarUsuario(id):
    dicUsuario = {'id': id}
    Usuario.eliminarUsuario(dicUsuario)
    return redirect('/usuarios')