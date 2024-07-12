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

    nuevas_ciudades["codigo_postal"] = input("Ingrese el codigo postal de la ciudad: ")

    nuevas_ciudades["poblacion"] = int(input("Ingrese la población de la ciudad: "))

    nuevas_ciudades["pais"] = input("Ingrese el país de la ciudad: ")

    nuevas_ciudades["moneda"] = input("Ingrese la moneda de la ciudad: ")

    nuevas_ciudades["idioma"] = input("Ingrese el idioma de la ciudad: ")

    print("La ciudad " + nuevas_ciudades["nombre"] + " fue agregada con Exito!!")

    ciudades["ciudades"].append(nuevas_ciudades)

    guardar_datos(ciudades, RUTA_JSON)


def eliminar_ciudad():
    ciudades = cargar_datos(RUTA_JSON)

    ciudad_eliminar = input("Ingrese el código postal de la ciudad que desea eliminar")
    contador = -1
    for i in ciudades["ciudades"]:
        contador += 1
        if(ciudad_eliminar == i["codigo_postal"]):
            ciudades["ciudades"].pop(contador)
            guardar_datos(ciudades, RUTA_JSON)

def actualizar_ciudades():
    ciudades = cargar_datos(RUTA_JSON)

    contador = 0

    codigo = input("Ingrese el código postal: ")

    for i in ciudades["ciudades"]:
        if(codigo == i["codigo_postal"]):
            contador = 1
            i["nombre"] = input("Ingrese el nuevo nombre de la ciudad: ")

            i["codigo_postal"] = int(input("Ingrese el nuevo codigó postal de la ciudad: "))

            i["poblacion"] = int(input("Ingrese la nueva población de la ciudad: "))

            i["pais"] = input("Ingrese el nuevo país de la ciudad: ")

            i["moneda"] = input("Ingrese la nueva moneda de la ciudad: ")

            i["idioma"] = input("Ingrese el nuevo idioma de la ciudad: ")

            guardar_datos(ciudades, RUTA_JSON)

    if(contador == 0):
        print("")
        print(f"La ciudad con el codigo postal {codigo} NO existe")
        print("")

    contador == 0


def busqueda_avanzada():
    ciudades = cargar_datos(RUTA_JSON)

    contador = 0

    dato = input("Ingrese el dato (Nombre, Pais o Codigó postal): ")


    for i in ciudades["ciudades"]:
        
        if(dato == i["nombre"]):
            contador = 1
            print("")
            print("DATOS DE LA CIUDAD")
            print("")
            print("Nombre: " + i["nombre"])
            print("Codigó Postal: " + str(i["codigo_postal"]))
            print("Población: " + str(i["poblacion"]))
            print("País: " + i["pais"])
            print("Moneda: " + i["moneda"])
            print("Idioma: " + i["idioma"])
            break
        elif(dato == i["pais"]):
            contador = 1
            print("")
            print("DATOS DE LA CIUDAD")
            print("")
            print("Nombre: " + i["nombre"])
            print("Codigó Postal: " + str(i["codigo_postal"]))
            print("Población: " + str(i["poblacion"]))
            print("País: " + i["pais"])
            print("Moneda: " + i["moneda"])
            print("Idioma: " + i["idioma"])
            break
        elif(dato == i["codigo_postal"] and contador == 0):
            contador = 1
            print("")
            print("DATOS DE LA CIUDAD")
            print("")
            print("Nombre: " + i["nombre"])
            print("Codigó Postal: " + str(i["codigo_postal"]))
            print("Población: " + str(i["poblacion"]))
            print("País: " + i["pais"])
            print("Moneda: " + i["moneda"])
            print("Idioma: " + i["idioma"])
            break

    if(contador == 0):
        print("")
        print(f"La ciudad con el dato {dato} NO existe")
        print("")

    contador = 0
        
def print_all():
    ciudades = cargar_datos(RUTA_JSON)
    print("------------------------------")
    for i in ciudades["ciudades"]:
        print(f"Ciudad = {i['nombre']}")
        print(f"Codigo Postal = {i['codigo_postal']}")
        print(f"Población estimada = {i['poblacion']}")
        print(f"Pais = {i['pais']}")
        print(f"Moneda = {i['moneda']}")
        print(f"Idioma = {i['idioma']}")
        print("------------------------------")
