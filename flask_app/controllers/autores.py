from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.autor import Autor
from flask_app.models.libro import Libro

@app.route('/')
def Inicio():
    return redirect('/autores')

@app.route('/autores')
def mostrarAutores():
    listaAutores = Autor.mostrarAutores()
    return render_template("autores.html", listaAutores = listaAutores)

@app.route('/crearAutor', methods = ['post'])
def crearAutor():
    dicAutor = {'nombre': request.form['nombre']}
    Autor.crearAutor(dicAutor)
    return redirect('/autores')

@app.route('/autor/<int:idAutor>')
def autorLibroFav(idAutor):
    dicIdAutor = {'idAutor': idAutor}
    listaLibrosNofav = Libro.mostrarLibrosNoFav(dicIdAutor)
    return render_template("autorLibroFav.html", autor = Autor.mostrarLibrosFavAutor(dicIdAutor), listaLibrosNofav = listaLibrosNofav)

@app.route('/anadirLibro', methods = ['post'])
def anadirLibroFavAutor():
    dicAutor = {'autorId': request.form['autorId'], 'libroId': request.form['libroId']}
    Autor.anadirFavAutor(dicAutor)
    return redirect('/autor/' + request.form['autorId'])
