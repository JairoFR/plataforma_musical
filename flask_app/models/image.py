import os
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo

class Image(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'fotos' #nombre de tabla
    columnas_tabla = [ 'artistas_id', 'image', 'usuarios_id' ] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.id = data['id'] 
        self.artistas_id = data['artistas_id'] 
        self.usuarios_id = data['usuarios_id'] 
        self.image = data['image']
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
    
    
    @classmethod
    def get_by_id_foto(cls, id):
        query = f"""SELECT fotos.image as foto from {cls.modelo}
                LEFT join artistas ON fotos.artistas_id =  artistas.artistas_id
                WHERE artistas.artistas_id= %(id)s;"""

        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        if len(results) > 0:
            return results
        else:
            return None 
    
    @classmethod
    def primera_foto(cls, id):
        query = f"SELECT * FROM fotos where fotos.artistas_id = %(id)s ORDER by ID DESC LIMIT 1;"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        if len(results) > 0:
            return results
        else:
            return None 
        
    @classmethod
    def primera_foto_usuario(cls, id):
        query = f"SELECT * FROM fotos where fotos.usuarios_id = %(id)s ORDER by ID DESC LIMIT 1;"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        if len(results) > 0:
            return results
        else:
            return None 
    @classmethod
    def save_photo_users(cls, data ):

        query = f"INSERT INTO {cls.modelo} (usuarios_id, image  ) VALUES (%(usuarios_id)s, %(image)s);"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db( query, data ) 
        print('resultado save base', resultado)
        return resultado

    @classmethod
    def save_photo_artistas(cls, data ):

        query = f"INSERT INTO {cls.modelo} (artistas_id, image  ) VALUES (%(artistas_id)s, %(image)s);"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db( query, data ) 
        print('resultado save base', resultado)
        return resultado



