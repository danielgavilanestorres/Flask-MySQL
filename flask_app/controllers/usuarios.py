from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.usuario import Usuario

@app.route('/')
def Inicio():
    return redirect('/amigos')

@app.route('/amigos')
def amigos():
    return render_template("amistades.html", amigos = Usuario.mostrarAmistades(), listaUsuarios = Usuario.todosLosUsuarios(), listaAmigos = Usuario.todosLosAmigos())

@app.route('/crearUsuario', methods=['post'])
def crearUsuario():
    dicUsuario = {'nombre': request.form['nombre'], 'apellido': request.form['apellido']}
    Usuario.crearUsuario(dicUsuario)
    return redirect('/amigos')

@app.route('/crearAmistad', methods=['post'])
def crearAmistad():
    dicUsuAmi = {'usuarioId': request.form['usuarioId'], 'amigoId': request.form['amigoId']}
    print(dicUsuAmi)
    Usuario.guardarAmistades(dicUsuAmi)
    return redirect('/amigos')

def consulta():
    print("Hola")