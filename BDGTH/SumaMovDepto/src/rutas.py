
from flask import Blueprint, render_template,  jsonify, request
from BDGTH.SumaMovDepto.src.database.db import ConexionSQL
import pyodbc


SumDepto = Blueprint("SumDepto", __name__, static_folder="static", template_folder="templates")


@SumDepto.route("/home")
@SumDepto.route("/")
def home():
    #return render_template("index.html")
    return "Estamos en la pagina de Suma de movimiento por departamento"

#@tipoNomina.route('/listarTiposDeNominas', methods=['GET'])
@SumDepto.route('/listarSumDepto', methods=['GET'])
def listar_SumDepto():

    con = ConexionSQL
    conn = con.conexion()
    cursor = conn.cursor()

    try:

        sql = '''

select *  from (
   SELECT 
     D.CLAVE_DEPARTAMENTO,D.DESCRIPCION, M.[MOV_TIPO], COUNT(*) AS TOTAL
     --M.[CLAVE_TRABAJADOR],M.[FECHA],M.[PRIOR_MOV],M.[MOV_TIPO],M.[CLAVE_TIPOS_BAJA],M.[CLAVE_CAUSA],M.[FECHA_IMSS]
     FROM [BDGTH].[dbo].[TRABMOVI] AS M 
     INNER JOIN TRABAJAD AS T ON M.CLAVE_TRABAJADOR = T.CLAVE_TRABAJADOR
     INNER JOIN TRAHISDE AS HD ON HD.CLAVE_TRABAJADOR = T.CLAVE_TRABAJADOR 
     INNER JOIN DEPARTAM AS D ON D.CLAVE_DEPARTAMENTO = HD.CLAVE_DEPARTAMENTO
     WHERE M.MOV_TIPO IN ('A','R','B') AND M.FECHA BETWEEN '20240401' AND '20240425'
      AND HD.CLAVE_DEPARTAMENTO IN (
      '111102','111107','111115','111121','111122','111172','112102','112107','112115','112120','112121','112122','112202','112207','112215',
      '112220','112221','112222','113102','113107','113115','113120','113121','113122','113172','114102','114107','114115','114120','114121',
      '114122','115002','120102','120107','120115','120120','120121','120122','120172','120202','120207','120215','120221','120320','130102',
      '130107','130115','130120','130121','130122','130123','130135','130136','130172','130202','130207','130215','130220','130221','130222',
      '140102','140107','140115','140120','140121','140122','140172','140202','140207','140215','140221','140222','150102','150107','150115',
      '150120','150121','150122','150202','150207','150215','150220','150221','150222','150235','150236','150320','180000','180002','1800P1',
      '1800P2','1800P3','1800P4','1800P5','1800P6','1800P7','1800P8','1800P9','1800R1','1800R2','T10100','T10400','T11100','T20300','T20400',
      'T20500','T21100','T21300','T21400','T30300','T41100','T41400','T41600','T41700','T51100','T51200','T51400','T54400','T54500'
     ) AND HD.FECHA_I <= '20240425' AND HD.FECHA_F >= '20240425'
     GROUP BY D.CLAVE_DEPARTAMENTO, D.DESCRIPCION, M.[MOV_TIPO]
     --ORDER BY D.CLAVE_DEPARTAMENTO, D.DESCRIPCION, M.[MOV_TIPO]
) as pivotTable
PIVOT (SUM(TOTAL) FOR MOV_TIPO in ([A],[R],[B])) AS pivotTable 
ORDER BY CLAVE_DEPARTAMENTO





'''

        cursor.execute(sql)
        datos = cursor.fetchall()
        #print(datos)
        lista = []

        for fila in datos:
            curso = {'DESCRIPCION':fila[1],'A': fila[2],'R': fila[3],'B': fila[4]}
            lista.append(curso)
        #return jsonify({'Tipos de nomina por mes':lista, 'mensaje':"Tipos de nominas"})
        print(lista)
        return jsonify(lista)

        
        
    #except Exception as ex:
    except pyodbc.Error as e:
        print("Ocurrió un error de SQL Server:", e)
        return jsonify({'mensaje': "Error"})



def pagina_no_encontrada(error):
    return '<h1>La pagina que intentas buscar no existe ...</h1>', 404







