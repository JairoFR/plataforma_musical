import os
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo

class Genero(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'generos' #nombre de tabla
    columnas_tabla = [ 'artistas_id', 'tipo'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.genero_id = data['genero_id'] 
        self.tipo = data['tipo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def destroy(cls,data):
        query  = f"DELETE FROM {cls.modelo} WHERE id = %(data)s;"
        data = { 'data': data}
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = f"UPDATE {cls.modelo} SET año_formacion = %(año_formacion)s, biografia = %(biografia)s, updated_at = NOW() WHERE artistas_id = %(artistas_id)s;"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
    
        return resultado

    @staticmethod
    def validar(data): 
        is_valid = True
   
        
        if len(data['username']) <= 3:
            flash(f'El Usuario no puede ser menor a 3', 'error')
            is_valid = False

        return is_valid
