import pyodbc

from flask import Blueprint



class ConexionSQL:

    
    def conexion():

        try:

                # Configuración de la conexión a SQL Server
            server = 'LAPTOP-PP6N1N88\SQLEXPRESS'
            database = 'BDGTH'
            username = 'sa'
            password = 'artesanos10'
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            
            return cnxn
        
        except Exception as ex:
            raise ex