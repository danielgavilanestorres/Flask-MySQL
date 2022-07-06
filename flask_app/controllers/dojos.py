from flask_app.models.dojo import Dojo
from flask import redirect, render_template, request
from flask_app import app

@app.route('/')
def Inicio():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    listaDojos = Dojo.mostrarDojos()
    return render_template("dojos.html", listaDojos = listaDojos)

@app.route('/nuevoDojo', methods = ['post'])
def nuevoDojo():
    dicDojo = {'nombre': request.form['nombre']}
    Dojo.crearDojo(dicDojo)
    return redirect('/dojos')

@app.route('/nuevoNinja')
def nuevoNinja():
    listaDojos = Dojo.mostrarDojos()
    return render_template("ninjas.html", listaDojos = listaDojos)

@app.route('/dojos/<int:id>')
def mostrarDojo(id):
    datosNinja = {'id': id}
    listaDojos = Dojo.mostrarNinjasDojo(datosNinja)
    return render_template("mostrarDojo.html", listaDojos=listaDojos)