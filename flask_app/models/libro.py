from flask_app.config.mysqlconnection import conectarMySQL
from flask_app.models import autor

class Libro:
    def __init__(self, datosLibro):
        self.idLibro = datosLibro['idLibro']
        self.titulo = datosLibro['titulo']
        self.numPaginas = datosLibro['numPaginas']
        self.fechaCreacion = datosLibro['fechaCreacion']
        self.fechaActualizacion = datosLibro['fechaActualizacion']
        self.favoritosAutor = []
    
    @classmethod
    def mostrarLibros(cls):
        consultaSQL = "select * from libros;"
        resultadoSQL = conectarMySQL('libros').operacionesBD(consultaSQL)
        listaLibros = []
        for libro in resultadoSQL:
            listaLibros.append(libro)
        return listaLibros
    
    @classmethod
    def crearLibro(cls, datosLibro):
        consultaSQL = "insert into libros(titulo, numPaginas, fechaCreacion, fechaActualizacion) values (%(titulo)s, %(numPaginas)s, now(), now());"
        return conectarMySQL('libros').operacionesBD(consultaSQL, datosLibro)
    
    @classmethod
    def mostrarLibrosNoFav(cls, dicIdAutor):
        consultaSQL = "select * from libros where libros.idLibro not in (select libroId from favoritos where autorId = %(idAutor)s);"
        resultadoSQL = conectarMySQL('libros').operacionesBD(consultaSQL, dicIdAutor)
        listaLibros = []
        for libro in resultadoSQL:
            listaLibros.append(libro)
        return listaLibros
    
    @classmethod
    def autoresLibros(cls, dicIdLibro):
        consultaSQL = "select * from autores left join favoritos on favoritos.autorId = autores.idAutor left join libros on favoritos.libroId = libros.idLibro where libroId = %(idLibro)s;"
        resultadoSQL = conectarMySQL('libros').operacionesBD(consultaSQL, dicIdLibro)
        objetoAutor = cls(resultadoSQL[0])
        for filabd in resultadoSQL:
            datos = {'idAutor': filabd['idAutor'], 'nombre': filabd['nombre'], 'fechaCreacion': filabd['fechaCreacion'], 'fechaActualizacion': filabd['fechaActualizacion']}
            objetoAutor.favoritosAutor.append(autor.Autor(datos))
        return objetoAutor

    @classmethod
    def anadirAutorFav(cls, dictAutorLibro):
        consultaSQL = "insert into favoritos(autorId, libroId) values(%(idAutor)s, %(idLibro)s);"
        print(consultaSQL)
        return conectarMySQL('libros').operacionesBD(consultaSQL, dictAutorLibro)



