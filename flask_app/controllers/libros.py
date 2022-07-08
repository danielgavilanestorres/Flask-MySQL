from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.libro import Libro
from flask_app.models.autor import Autor

@app.route('/libros')
def libros():
    listaLibros = Libro.mostrarLibros()
    return render_template("libros.html", listaLibros = listaLibros)

@app.route('/crearLibro', methods = ['post'])
def crearLibros():
    dicLibro = {'titulo': request.form['ftitulo'], 'numPaginas': request.form['fnumPaginas']} 
    Libro.crearLibro(dicLibro)
    return redirect('/libros')

@app.route('/libro/<int:idLibro>')
def libroAutor(idLibro):
    dicIdLibro = {'idLibro': idLibro}
    listaAutores = Autor.mostrarAutoresNoFav(dicIdLibro)
    return render_template("libroAutorFav.html", libro = Libro.autoresLibros(dicIdLibro), listaAutores = listaAutores)

@app.route('/anadirAutor', methods = ['post'])
def anadirAutorFav():
    dicAutorLibro = {'idAutor' : request.form['autorId'], 'idLibro': request.form['libroId']}
    print(dicAutorLibro)
    Libro.anadirAutorFav(dicAutorLibro)
    return redirect('libro/' + request.form['libroId'])
