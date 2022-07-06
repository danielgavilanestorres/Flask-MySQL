from flask_app.config.mysqlconnection import conectarMySQL

class Ninja:
    def __init__(self, datosNinja):
        self.id = datosNinja['id']
        self.nombre = datosNinja['nombre']
        self.apellido = datosNinja['apellido']
        self.edad = datosNinja['edad']
        self.fechaCreacion = datosNinja['fechaCreacion']
        self.fechaActualizacion = datosNinja['fechaActualizacion']
    
    @classmethod
    def nuevoNinja(cls, datosNinja):
        consultaSQL = "insert into ninjas(nombre, apellido, edad, fechaCreacion, fechaActualizacion, dojo_id) values(%(nombre)s, %(apellido)s, %(edad)s, now(), now(), %(dojo_id)s);"
        return conectarMySQL('dojosyninjas').operacionBD(consultaSQL, datosNinja)
    