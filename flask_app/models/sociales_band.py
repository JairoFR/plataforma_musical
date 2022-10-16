import os
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo


class Social(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'sociales_band' #nombre de tabla
    columnas_tabla = [ 'artistas_id', 'link', 'red_social'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.sociales_band_id = data['sociales_band_id'] 
        self.artistas_id = data['artistas_id'] 
        self.link = data['link']
        self.red_social = data['red_social']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def destroy(cls,data):
        query  = f"DELETE FROM {cls.modelo} WHERE social_band_id = %(data)s;"
        data = { 'data': data}
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,data)

    @staticmethod
    def validar(data): 
        is_valid = True
   
        
        if len(data['username']) <= 3:
            flash(f'El Usuario no puede ser menor a 3', 'error')
            is_valid = False

        return is_valid
