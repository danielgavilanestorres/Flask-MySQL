from flask import request
from flask_app.config.mysqlconnection import conectarMySQL

class Usuario:
    def __init__(self, datosUsuario):
        self.id = datosUsuario['id']
        self.nombre = datosUsuario['nombre']
        self.apellido = datosUsuario['apellido']
        self.fechaCreacion = datosUsuario['fechaCreacion']
        self.fechaActualizacion = datosUsuario['fechaActualizacion']
        self.amigos = []
    
    @classmethod
    def crearUsuario(cls, datosUsuario):
        consultaSQL = "insert into usuarios(nombre, apellido) values(%(nombre)s, %(apellido)s);"
        return conectarMySQL('amistades').operacionesBD(consultaSQL, datosUsuario)
    
    @classmethod
    def mostrarAmistades(cls):
        consultaSQL = "select * from usuarios as u inner join amistades as a on a.usuarioId = u.id inner join usuarios as u2 on u2.id = a.amigoId;"
        resultadosSQL = conectarMySQL('amistades').operacionesBD(consultaSQL)
        objetoAmigos = cls(resultadosSQL[0])
        for filabd in resultadosSQL:
            data = {'id': filabd['id'], 'nombre': filabd['nombre'], 'apellido': filabd['apellido'], 'amigoId': filabd['amigoId'], 'nombreAmigo': filabd['u2.nombre'], 'apellidoAmigo': filabd['u2.apellido']}
            objetoAmigos.amigos.append(data)
        return objetoAmigos
    
    @classmethod
    def todosLosUsuarios(cls):
        consultaSQL = "select * from usuarios;"
        resultadoSQL = conectarMySQL('amistades').operacionesBD(consultaSQL)
        listaUsuarios = []
        for usuario in resultadoSQL:
            listaUsuarios.append(usuario)
        return listaUsuarios

    @classmethod
    def todosLosAmigos(cls):
        consultaSQL = "select * from usuarios as u where u.id not in (select a.amigoId from amistades as a where a.usuarioId = 1);"
        resultadoSQL = conectarMySQL('amistades').operacionesBD(consultaSQL)
        listaAmigos = []
        for usuario in resultadoSQL:
            listaAmigos.append(usuario)
        return listaAmigos
    
    @classmethod
    def guardarAmistades(cls, dicUsuAmi):
        consultaSQL = "insert into amistades(usuarioId, amigoId) values(%(usuarioId)s, %(amigoId)s);"
        print(consultaSQL)
        return conectarMySQL('amistades').operacionesBD(consultaSQL, dicUsuAmi)
    

