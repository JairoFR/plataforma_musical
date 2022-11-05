import os
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo


class Social(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'sociales_band' #nombre de tabla
    columnas_tabla = [ 'artistas_id', 'facebook', 'youtube', 'amazon_music', 'apple_music', 'instagram', 'spotify', 'tidal'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.sociales_band_id = data['sociales_band_id'] 
        self.facebook = data['facebook']    
        self.youtube = data['youtube']    
        self.amazon_music = data['amazon_music']    
        self.apple_music = data['apple_music']    
        self.instagram = data['instagram']    
        self.spotify = data['spotify']        
        self.tidal = data['tidal']    
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

    @classmethod
    def get_by_id_redes(cls, id):
        query = f"""SELECT sociales_band.red_social as redes, sociales_band.link FROM {cls.modelo}
                LEFT join artistas ON sociales_band.artistas_id =  artistas.artistas_id
                WHERE artistas.artistas_id= %(id)s;"""

        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        print('get_by_id_redes', results)
        if len(results) > 0:
            return results
        else:
            return None 
