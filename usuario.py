from asyncio import constants
from mysqlconnection import conectarMySQL

class Usuario:
    def __init__(self, datosUsuario):
        self.id = datosUsuario['id']
        self.nombre = datosUsuario['nombre']
        self.apellido = datosUsuario['apellido']
        self.correo = datosUsuario['correo']
        self.fechaCreacion = datosUsuario['fechaCreacion']
        self.fechaActualizacion = datosUsuario['fechaActualizacion']
    
    @classmethod
    def mostrarTodo(cls):
        consultaSQL = "select * from usuarios;"
        resuladoconsultaSQL = conectarMySQL('usuariosmysql').operacionBD(consultaSQL)
        listaUsuarios = []
        for usuario in resuladoconsultaSQL:
            listaUsuarios.append(usuario)
        return listaUsuarios
    
    @classmethod
    def crearUsuario(cls, usuario):
        consultaSQL = "insert into usuarios(nombre, apellido, correo, fechaCreacion, fechaActualizacion) values (%(fnombre)s, %(fapellido)s, %(fcorreo)s, now(), now())"        
        return conectarMySQL('usuariosmysql').operacionBD(consultaSQL, usuario)

    @classmethod
    def mostrarUsuarioId(cls, datosUsuario):
        consultaSQL = "select id, nombre, apellido, correo, fechaCreacion, fechaActualizacion from usuarios where id = %(id)s"
        resultadoSQL = conectarMySQL('usuariosmysql').operacionBD(consultaSQL, datosUsuario)
        usuario = []
        for u in resultadoSQL:
            usuario.append(u)
        return usuario
    
    @classmethod
    def actualizarUsuario(cls, datosUsuario):
        consultaSQL = "update usuarios set nombre = %(fnombre)s, apellido = %(fapellido)s, correo = %(fcorreo)s, fechaActualizacion = now() where id = %(id)s ;"
        print(consultaSQL)
        return conectarMySQL('usuariosmysql').operacionBD(consultaSQL, datosUsuario)
    
    @classmethod
    def eliminarUsuario(cls, datosUsuario):
        consultaSQL = "delete from usuarios where id = %(id)s"
        return conectarMySQL('usuariosmysql').operacionBD(consultaSQL, datosUsuario)
