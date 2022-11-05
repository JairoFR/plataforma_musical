import os
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Artista(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'artistas' #nombre de tabla
    columnas_tabla = [ 'username', 'email', 'password','biografia', 'año_formacion'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.artistas_id = data['artistas_id'] 
        self.direcciones_id = data['direcciones_id'] 
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.biografia = data['biografia']
        self.año_formacion = data['año_formacion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save_usuario(cls, data ):
        query = f"""INSERT INTO {cls.modelo} ( username, email, password, created_at, updated_at ) 
                VALUES ( %(username)s, %(email)s, %(password)s, NOW() , NOW() );"""

        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db( query, data ) 
        print('resultado save', resultado)
        return resultado

    @classmethod
    def get_by_id(cls, data):
        query = f"SELECT * FROM {cls.modelo} where artistas_id = %(data)s;"
        data = { 'data' : data }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
    
        all_data = []

        for data in results:
            all_data.append( cls(data) )
        return all_data

    @classmethod
    def get_by_email(cls, data):
        
        query = f"SELECT * FROM {cls.modelo} WHERE  email = %(data)s"
        data = { 'data': data }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        # no se encontró un usuario coincidente
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = f"""UPDATE {cls.modelo} 
                    SET username = %(username)s, email = %(email)s, biografia = %(biografia)s, año_formacion= %(año_formacion)s, updated_at = NOW() 
                    WHERE artistas_id = %(artistas_id)s;"""

        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        return resultado
    @classmethod
    def get_fotos_username(cls):
        query = f"""SELECT artistas.username as username, fotos.image as foto, artistas.artistas_id as id FROM artistas
                    JOIN fotos ON artistas.artistas_id = fotos.artistas_id;"""
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query)
        return results
        

    @staticmethod
    def validar(data): 
        is_valid = True
        if len(data['username']) <= 3:
            flash(f'El nombre no puede ser menor a 3', 'error')
            is_valid = False

        if not EMAIL_REGEX.match(data['email']): 
            flash("Direccion de email invalida!","error")
            is_valid = False

        return is_valid

    @staticmethod
    def validar_pass(data): 
        is_valid = True

        query = "SELECT * FROM usuarios WHERE email = %(data)s;"
        dato = {'data': data['email']}
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,dato) 
      

        if len(results) >= 1:
            flash("Email ya existe.","error")
            is_valid=False
        
        if data['password'] != data['cpassword']:
            is_valid = False
            flash("Las contraseñas no coinciden!","error")
        
        if len(data['password']) < 8:
            is_valid = False
            flash("La contraseña debe tener minimo de 8 caracteres", 'error')

        return is_valid



 