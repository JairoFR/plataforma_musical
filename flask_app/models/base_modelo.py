import os
from flask_app.config.mysqlconnection import connectToMySQL

class BaseModelo:

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {cls.modelo} ;"
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query)
        print(results, '>>>>>>>>>>>>>>>')
        all_data = []

        for data in results:
            all_data.append( cls(data) )
        return all_data
    
    @classmethod
    def destroy(cls,data):
        print('entro a destroy', data)
        query  = f"DELETE FROM {cls.modelo} WHERE artistas_id = %(data)s;"
        data = { 'data': data}
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,data)
    
    
    @classmethod
    def save(cls, data ):

        columnas = ''
        filas = ''
        for columna in cls.columnas_tabla:
            columnas +=columna + ','
            filas += f'%({columna})s,' 

        query = f"INSERT INTO {cls.modelo} ( {columnas}created_at, updated_at ) VALUES ( {filas}NOW() , NOW() );"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db( query, data ) 
        print('resultado save base', resultado)
        return resultado
    
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {cls.modelo} where artistas_id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        if len(results) > 0:
            return results
        else:
            return None 

    @classmethod
    def update(cls,data):

        columnas = ''
        for columna in cls.columnas_tabla:
            columnas +=f'{columna}=%({columna})s,' 

        query = f"UPDATE {cls.modelo} SET {columnas}update_at=NOW() WHERE id = %(id)s;"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado
