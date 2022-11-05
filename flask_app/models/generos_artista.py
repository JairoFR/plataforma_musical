import os
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo

class Generos_artista(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'generos_artista' #nombre de tabla
    columnas_tabla = [] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.generos_artista_id = data['generos_artista_id'] 
        self.genero_id = data['genero_id'] 
        self.artistas_id = data['artistas_id'] 
    
    @classmethod
    def save(cls, data ):

        query = f"INSERT INTO {cls.modelo} (genero_id, artistas_id  ) VALUES (%(genero_id)s, %(artistas_id)s);"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db( query, data ) 
        print('resultado save base', resultado)
        return resultado

    @classmethod
    def destroy(cls,data):
        query  = f"DELETE FROM {cls.modelo} WHERE generos_artista_id = %(data)s;"
        data = { 'data': data}
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = f"UPDATE {cls.modelo} SET año_formacion = %(año_formacion)s, biografia = %(biografia)s, updated_at = NOW() WHERE artistas_id = %(artistas_id)s;"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        return resultado

    # -- obtener generos por artista en session
    @classmethod
    def generos(cls, id):
        print(id)
        query = f"""SELECT generos_artista.* ,generos.tipo as tipo from artistas
                join generos_artista on artistas.artistas_id = generos_artista.artistas_id
                join generos on generos_artista.genero_id = generos.genero_id
                where artistas.artistas_id = %(id)s;"""
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        if len(results) > 0:
            return results
        else:
            return None 

    @staticmethod
    def validar(data): 
        is_valid = True
   
        
        if len(data['username']) <= 3:
            flash(f'El Usuario no puede ser menor a 3', 'error')
            is_valid = False

        return is_valid
