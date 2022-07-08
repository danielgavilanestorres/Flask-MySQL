from flask_app.config.mysqlconnection import conectarMySQL
from flask_app.models import libro

class Autor:
    def __init__(self, datosAutor):
        self.idAutor = datosAutor['idAutor']
        self.nombre = datosAutor['nombre']
        self.fechaCreacion = datosAutor['fechaCreacion']
        self.fechaActualizacion = datosAutor['fechaActualizacion']
        self.librosFavoritos = []

    @classmethod
    def mostrarAutores(cls):
        consultaSQL = "select * from autores;"
        resultadoSQL = conectarMySQL('libros').operacionesBD(consultaSQL)
        listaAutores = []
        for autor in resultadoSQL:
            listaAutores.append(autor)
        return listaAutores
    
    @classmethod
    def crearAutor(cls, datosAutor):
        consultaSQL = "insert into autores(nombre, fechaCreacion, fechaActualizacion) values (%(nombre)s, now(), now());"
        return conectarMySQL('libros').operacionesBD(consultaSQL, datosAutor)
    
    @classmethod
    def mostrarAutorId(cls, dicIdAutor):
        consultaSQL = "select * from autores where idAutor = %(idAutor)s;"
        resultadoSQL = conectarMySQL('libros').operacionesBD(consultaSQL, dicIdAutor)
        return cls(resultadoSQL[0])
    
    @classmethod
    def mostrarLibrosFavAutor(cls, dicIdAutor):
        consultaSQL = "select * from autores left join favoritos on autores.idAutor = favoritos.autorId left join libros on libros.idLibro = favoritos.libroId where autores.idAutor = %(idAutor)s;"
        resultadoSQL = conectarMySQL('libros').operacionesBD(consultaSQL, dicIdAutor)
        objetoAutor = cls(resultadoSQL[0])
        for filabd in resultadoSQL: 
            datos = {'idLibro': filabd['idLibro'], 'titulo': filabd['titulo'], 'numPaginas': filabd['numPaginas'], 'fechaCreacion': filabd['libros.fechaCreacion'], 'fechaActualizacion': filabd['libros.fechaActualizacion']}
            objetoAutor.librosFavoritos.append(libro.Libro(datos))
        return objetoAutor
    
    @classmethod
    def anadirFavAutor(cls, datosAutorLibro):
        consultaSQL = "insert into favoritos(autorId, libroId) values(%(autorId)s, %(libroId)s);"
        return conectarMySQL('libros').operacionesBD(consultaSQL, datosAutorLibro)

    @classmethod
    def mostrarAutoresNoFav(cls, dicIdLibro):
        consultaSQL = "select * from autores where autores.idAutor not in (select autorId from favoritos where libroId = %(idLibro)s);"
        resultadoSQL = conectarMySQL('libros').operacionesBD(consultaSQL, dicIdLibro)
        listaAutores = []
        for autor in resultadoSQL:
            listaAutores.append(autor)
        return listaAutores