import sys
import os

sys.path.append("..")

from datosGenerales.datos import *
from modulo_reportes.reportes_excepciones import agregar_reportes

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RUTA_JSON = os.path.join(project_root,  "MODULO_DATOS", "ciudades.json")


def agregar_ciudad():
    ciudades = cargar_datos(RUTA_JSON)

    for i in ciudades:
        print(i)

agregar_ciudad()