import sys
import os

sys.path.append('D:\\alejandro\\API base de datos')

from app import app as aplication
aplication.secret_key = 'anythingwished'