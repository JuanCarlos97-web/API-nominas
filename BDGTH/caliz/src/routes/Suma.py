

from flask import Blueprint, jsonify, request

# Entities
from BDGTH.caliz.src.models.entities.suma import Suma

# Models
from BDGTH.caliz.src.models.SumaModelo import SumaModelo

sumaMov = Blueprint('sumaMov',__name__)

@sumaMov.route('/')
def get_sumaMov():
    try:
        sumasMov = SumaModelo.get_sumaMov()
        print(sumasMov)
        return jsonify(sumasMov)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500