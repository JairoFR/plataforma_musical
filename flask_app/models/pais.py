import os
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo


class Pais(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'paises' #nombre de tabla
    columnas_tabla = [ 'nombre'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.pais_id = data['pais_id'] 
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    @classmethod
    def get_by_id(cls, data):
        
        query = "SELECT * FROM usuarios WHERE  id = %(data)s"
        data = { 'data': data }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)

        # no se encontró un usuario coincidente
        all_data = []

        for data in results:
            all_data.append( cls(data) )
        return all_data
    

    @classmethod
    def update(cls,data):
        query = f"UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
    
        return resultado
    


