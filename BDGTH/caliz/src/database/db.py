import pyodbc


from decouple import config


    
def conexion():

    try:

            # Configuración de la conexión a SQL Server
        server = config('SQL_HOST')
        database = config('SQL_DB')
        username = config('SQL_USER')
        password = config('SQL_PASSWORD')
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        
        return cnxn
    
    except Exception as ex:
        raise ex