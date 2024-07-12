import sys
import os

sys.path.append("..")

from MODULO_DATOS.datos import *

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RUTA_JSON = os.path.join(project_root,  "MODULO_DATOS", "ciudades.json")

def agregar_ciudad():
    ciudades = cargar_datos(RUTA_JSON)

    nuevas_ciudades = {}

    contador_ciudades = 0

    for i in ciudades["ciudades"]:
        contador_ciudades += 1
        print(i)

    nuevas_ciudades["id"] = contador_ciudades + 1

    nuevas_ciudades["nombre"] = input("Ingrese el nombre de la ciudad: ")

    nuevas_ciudades["codigo_postal"] = int(input("Ingrese el codigo postal de la ciudad: "))

    nuevas_ciudades["población"] = int(input("Ingrese la población de la ciudad: "))

    nuevas_ciudades["pais"] = input("Ingrese el país de la ciudad: ")

    nuevas_ciudades["moneda"] = input("Ingrese la moneda de la ciudad: ")

    nuevas_ciudades["idioma"] = input("Ingrese el idioma de la ciudad: ")

    print("La ciudad " + nuevas_ciudades["nombre"] + " fue agregada con Exito!!")

    ciudades["ciudades"].append(nuevas_ciudades)

    guardar_datos(ciudades, RUTA_JSON)