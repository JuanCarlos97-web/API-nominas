
from flask import Blueprint, render_template,  jsonify, request
from .database.db import ConexionSQL


tipoNomina = Blueprint("tipoNomina", __name__, static_folder="static", template_folder="templates")


@tipoNomina.route("/home")
@tipoNomina.route("/")
def home():
    #return render_template("index.html")
    return "Estamos en la pagina de tipo de nomina"

#@tipoNomina.route('/listarTiposDeNominas', methods=['GET'])
@tipoNomina.route('/listarTiposDeNominas/<mes>', methods=['GET'])
def listar_nominas(mes):

    con = ConexionSQL
    conn = con.conexion()
    cursor = conn.cursor()

    try:
        #cursor = conn.conexion.cursor()
        #cursor = conexion.conexion.cursor()
        sql = "SELECT UPPER(P.MES_ACUMULACION) MES, N.CLAVE_TIPO_NOMINA  FROM   [BDGTH].[dbo].[CONCEPTO] C        ,BDGTH.[dbo].[TRABNOMI] N        ,[BDGTH].[dbo].[TRABAJAD] T        ,[BDGTH].[dbo].[TRAHISSU] HS        ,[BDGTH].[dbo].[SUCURSAL] CS        ,[BDGTH].[dbo].[REGIPATR] CR        ,[BDGTH].[dbo].[TRAHISDE] HD        ,[BDGTH].[dbo].[DEPARTAM] CD        ,[BDGTH].[dbo].[CENTCOST] CC        ,[BDGTH].[dbo].[PERIODO] P        ,[BDGTH].[dbo].[TIPONOMI] TN  WHERE              N.TOTAL <> 0          AND (C.CONCEPTO_PDC = 'P' OR C.CLAVE_CONCEPTO = 'PERC' )  AND N.CLAVE_TRABAJADOR = T.CLAVE_TRABAJADOR  AND N.CLAVE_CONCEPTO = C.CLAVE_CONCEPTO  AND N.CLAVE_TIPO_NOMINA = P.CLAVE_TIPO_NOMINA  AND N.CLAVE_PERIODO = P.CLAVE_PERIODO  AND (UPPER(P.MES_ACUMULACION) = '{0}'  ) AND P.EJERCICIO = 2024 AND P.CERRADO = '1' AND P.CLAVE_TIPO_NOMINA = TN.CLAVE_TIPO_NOMINA  AND N.CLAVE_TRABAJADOR = HS.CLAVE_TRABAJADOR  AND HS.FECHA_I <= P.FECHA_F AND HS.FECHA_F >= P.FECHA_F  AND HS.CLAVE_SUCURSAL = CS.CLAVE_SUCURSAL  AND CS.CLAVE_REGPAT   = CR.CLAVE_REGPAT  AND N.CLAVE_TRABAJADOR = HD.CLAVE_TRABAJADOR  AND HD.FECHA_I <= P.FECHA_F AND HD.FECHA_F >= P.FECHA_F  AND HD.CLAVE_DEPARTAMENTO = CD.CLAVE_DEPARTAMENTO  AND CD.CLAVE_CENTR_COSTO  = CC.CLAVE_CENTR_COSTO  GROUP BY          N.CLAVE_TIPO_NOMINA,          TN.DESCRIPCION,           CR.RFC_EMISOR,           CR.NOMBRE,           CS.CLAVE_SUCURSAL,           CS.DESCRIPCION,   CD.CLAVE_CENTR_COSTO,   CC.DESCRIPCION,   CD.CLAVE_DEPARTAMENTO,   CD.DESCRIPCION,   P.MES_ACUMULACION   , N.CLAVE_CONCEPTO   , C.DESCRIPCION    ORDER BY          N.CLAVE_TIPO_NOMINA,          TN.DESCRIPCION,           CR.RFC_EMISOR,           CR.NOMBRE,           CS.CLAVE_SUCURSAL,           CS.DESCRIPCION,   CD.CLAVE_CENTR_COSTO,   CC.DESCRIPCION,   CD.CLAVE_DEPARTAMENTO,   CD.DESCRIPCION,   P.MES_ACUMULACION   , N.CLAVE_CONCEPTO   , C.DESCRIPCION".format(mes)

        #sql = "SELECT UPPER(P.MES_ACUMULACION) MES, N.CLAVE_TIPO_NOMINA  FROM   [BDGTH].[dbo].[CONCEPTO] C        ,BDGTH.[dbo].[TRABNOMI] N        ,[BDGTH].[dbo].[TRABAJAD] T        ,[BDGTH].[dbo].[TRAHISSU] HS        ,[BDGTH].[dbo].[SUCURSAL] CS        ,[BDGTH].[dbo].[REGIPATR] CR        ,[BDGTH].[dbo].[TRAHISDE] HD        ,[BDGTH].[dbo].[DEPARTAM] CD        ,[BDGTH].[dbo].[CENTCOST] CC        ,[BDGTH].[dbo].[PERIODO] P        ,[BDGTH].[dbo].[TIPONOMI] TN  WHERE              N.TOTAL <> 0          AND (C.CONCEPTO_PDC = 'P' OR C.CLAVE_CONCEPTO = 'PERC' )  AND N.CLAVE_TRABAJADOR = T.CLAVE_TRABAJADOR  AND N.CLAVE_CONCEPTO = C.CLAVE_CONCEPTO  AND N.CLAVE_TIPO_NOMINA = P.CLAVE_TIPO_NOMINA  AND N.CLAVE_PERIODO = P.CLAVE_PERIODO  AND (UPPER(P.MES_ACUMULACION) = 'ENERO'  OR  UPPER(P.MES_ACUMULACION) = 'FEBRERO') AND P.EJERCICIO = 2024 AND P.CERRADO = '1' AND P.CLAVE_TIPO_NOMINA = TN.CLAVE_TIPO_NOMINA  AND N.CLAVE_TRABAJADOR = HS.CLAVE_TRABAJADOR  AND HS.FECHA_I <= P.FECHA_F AND HS.FECHA_F >= P.FECHA_F  AND HS.CLAVE_SUCURSAL = CS.CLAVE_SUCURSAL  AND CS.CLAVE_REGPAT   = CR.CLAVE_REGPAT  AND N.CLAVE_TRABAJADOR = HD.CLAVE_TRABAJADOR  AND HD.FECHA_I <= P.FECHA_F AND HD.FECHA_F >= P.FECHA_F  AND HD.CLAVE_DEPARTAMENTO = CD.CLAVE_DEPARTAMENTO  AND CD.CLAVE_CENTR_COSTO  = CC.CLAVE_CENTR_COSTO  GROUP BY          N.CLAVE_TIPO_NOMINA,          TN.DESCRIPCION,           CR.RFC_EMISOR,           CR.NOMBRE,           CS.CLAVE_SUCURSAL,           CS.DESCRIPCION,   CD.CLAVE_CENTR_COSTO,   CC.DESCRIPCION,   CD.CLAVE_DEPARTAMENTO,   CD.DESCRIPCION,   P.MES_ACUMULACION   , N.CLAVE_CONCEPTO   , C.DESCRIPCION    ORDER BY          N.CLAVE_TIPO_NOMINA,          TN.DESCRIPCION,           CR.RFC_EMISOR,           CR.NOMBRE,           CS.CLAVE_SUCURSAL,           CS.DESCRIPCION,   CD.CLAVE_CENTR_COSTO,   CC.DESCRIPCION,   CD.CLAVE_DEPARTAMENTO,   CD.DESCRIPCION,   P.MES_ACUMULACION   , N.CLAVE_CONCEPTO   , C.DESCRIPCION"
        cursor.execute(sql)
        datos = cursor.fetchall()
        #print(datos)
        lista = []

        for fila in datos:
            curso = {'MES':fila[0],'CLAVE_TIPO_NOMINA': fila[1]}
            lista.append(curso)
        #return jsonify({'Tipos de nomina por mes':lista, 'mensaje':"Tipos de nominas"})
        return jsonify(lista)

        #print(datos)
        
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


def pagina_no_encontrada(error):
    return '<h1>La pagina que intentas buscar no existe ...</h1>', 404

'''
if __name__ == '__main__':
    tipoNomina.config.from_object(config['development'])
    tipoNomina.register_error_handler(404, pagina_no_encontrada)
    tipoNomina.run()
'''





