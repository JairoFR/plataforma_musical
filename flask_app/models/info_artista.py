import os
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo



class Info_artista(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'info_artistas' #nombre de tabla
    columnas_tabla = [ 'año_formacion', 'biografia', 'artistas_id'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.info_artista_id = data['info_artistas_id'] 
        self.artistas_id = data['artistas_id'] 
        self.año_formacion = data['año_formacion']
        self.biografia = data['biografia']   
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def update(cls,data):
        query = f"UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
    
        return resultado
    

    @staticmethod
    def validar(data): 
        is_valid = True
   
        
        if len(data['username']) <= 3:
            flash(f'El Usuario no puede ser menor a 3', 'error')
            is_valid = False

        return is_valid




