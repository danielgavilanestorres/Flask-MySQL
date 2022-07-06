from flask_app.config.mysqlconnection import conectarMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, datosDojo):
        self.id = datosDojo['id']
        self.nombre = datosDojo['nombre']
        self.fechaCreacion = datosDojo['fechaCreacion']
        self.fechaActualizacion = datosDojo['fechaActualizacion']
        self.ninjas = []
    
    @classmethod
    def crearDojo(cls, datosDojo):
        consultaSQL = "insert into dojos(nombre, fechaCreacion, fechaActualizacion) values (%(nombre)s, now(), now());"
        return conectarMySQL('dojosyninjas').operacionBD(consultaSQL, datosDojo)
    
    @classmethod
    def mostrarDojos(cls):
        consultaSQL = "select * from dojos;"
        resultadoSQL = conectarMySQL('dojosyninjas').operacionBD(consultaSQL)
        listaDojos = []
        for dojo in resultadoSQL:
            listaDojos.append(dojo)
        return listaDojos
    
    @classmethod
    def mostrarNinjasDojo(cls, datosNinja):
        consultaSQL = "select * from ninjas left join dojos on ninjas.dojo_id = dojos.id where ninjas.dojo_id = %(id)s;"
        resultadoSQL = conectarMySQL('dojosyninjas').operacionBD(consultaSQL, datosNinja)
        dojo = cls(resultadoSQL[0])

        for filaNinja in resultadoSQL:
            listaNinja = {
                'id': filaNinja['id'],
                'nombre': filaNinja['nombre'], 
                'apellido': filaNinja['apellido'], 
                'edad': filaNinja['edad'],
                'fechaCreacion': filaNinja['fechaCreacion'],
                'fechaActualizacion': filaNinja['fechaActualizacion']
                }
            dojo.ninjas.append(Ninja(listaNinja))
        return dojo.ninjas


