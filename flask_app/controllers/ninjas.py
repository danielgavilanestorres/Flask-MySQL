from flask import redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/guardar/Ninja', methods = ['post'])
def guardarNinja():
    dicNinja = {'nombre': request.form['nombre'], 'apellido': request.form['apellido'], 'edad': request.form['edad'], 'dojo_id': request.form['dojo_id']}
    Ninja.nuevoNinja(dicNinja)
    return redirect('/dojos')