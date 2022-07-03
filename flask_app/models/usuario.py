from flask_app.config.mysqlconnection import conectarMySQL

class Usuario:
    def __init__(self, datosUsuario):
        self.id = datosUsuario['id']
        self.nombre = datosUsuario['nombre']
        self.apellido = datosUsuario['apellido']
        self.correo = datosUsuario['correo']
        self.fechaCreacion = datosUsuario['fechaCreacion']
        self.fechaActualizacion = datosUsuario['fechaActualizacion']
    
    @classmethod
    def mostrarTodosUsuarios(cls):
        consultaSQL = "select * from usuarios;"
        resultadoSQL = conectarMySQL('usuariosmysql').operacionBD(consultaSQL)
        listaUsuarios = [] 
        for usuario in resultadoSQL:
            listaUsuarios.append(usuario)
        return listaUsuarios
    
    @classmethod
    def nuevoUsuario(cls, datosUsuario):
        consultaSQL = "insert into usuarios(nombre, apellido, correo, fechaCreacion, fechaActualizacion) values (%(fnombre)s, %(fapellido)s, %(fcorreo)s, now(), now())"
        return conectarMySQL('usuariosmysql').operacionBD(consultaSQL, datosUsuario)

    @classmethod
    def mostrarUnUsuario(cls, datosUsuario):
        consultaSQL = "select * from usuarios where id = %(id)s"
        resultadoSQL = conectarMySQL('usuariosmysql').operacionBD(consultaSQL, datosUsuario)
        return cls(resultadoSQL[0])
    
    @classmethod
    def editarUsuario(cls, datosUsuario):
        consultaSQL = "update usuarios set nombre = %(fnombre)s, apellido = %(fapellido)s, correo = %(fcorreo)s, fechaActualizacion = now() where id = %(id)s;"
        return conectarMySQL('usuariosmysql').operacionBD(consultaSQL, datosUsuario)
    
    @classmethod
    def eliminarUsuario(cls, datosUsuario):
        consultaSQL = "delete from usuarios where id = %(id)s"
        return conectarMySQL('usuariosmysql').operacionBD(consultaSQL, datosUsuario)