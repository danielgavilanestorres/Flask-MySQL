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
    def seleccionarTodo(cls):
        consultaQuery = "select * from usuarios;"
        resultadoConsulta = conectarMySQL('usuariosmysql').consultaBD(consultaQuery)
        usuarios = []
        for usuario in resultadoConsulta:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def crearUsuario(cls, datosUsuario):
        consulta = "insert into usuarios(nombre, apellido, correo, fechaCreacion, fechaActualizacion) values (%(fnombre)s, %(fapellido)s, %(fcorreo)s, now(), now());"
        return conectarMySQL('usuariosmysql').consultaBD(consulta, datosUsuario)

    
