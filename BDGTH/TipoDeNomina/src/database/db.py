import pyodbc

from flask import Blueprint
from decouple import config



class ConexionSQL:

    
    def conexion():

        try:

            '''
                           # Configuración de la conexión a SQL Server
            server = 'LAPTOP-PP6N1N88\SQLEXPRESS'
            database = 'BDGTH'
            username = 'sa'
            password = 'artesanos10'
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            '''

                # Configuración de la conexión a SQL Server
            server = config('SQL_HOST')
            database = config('SQL_DB')
            username = config('SQL_USER')
            password = config('SQL_PASSWORD')
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            
            return cnxn
        
        except Exception as ex:
            raise ex