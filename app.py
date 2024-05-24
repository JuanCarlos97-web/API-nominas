

from flask import Flask, render_template
from BDGTH.TipoDeNomina.src.rutas import tipoNomina
from BDGTH.SumaMovDepto.src.rutas import SumDepto
#from peliculas.peliculas import peliculas
#from series_tv.series import series
from BDGTH.caliz.src.routes import Suma
from waitress import serve


app = Flask(__name__)
app.register_blueprint(tipoNomina, url_prefix="/tipoDeNomina")
app.register_blueprint(SumDepto, url_prefix="/sumaMovDepto" )
app.register_blueprint(Suma.sumaMov, url_prefix='/sumMovDepto2')
SumDepto

@app.route("/")
def test():
    return "<h1>Pagina de incio</h1>"


def pagina_no_encontrada(error):
    return '<h1>La pagina que intentas buscar no existe ...</h1>', 404

if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    serve(app, host='0.0.0.0', port=5000)
    #app.run(debug=True)