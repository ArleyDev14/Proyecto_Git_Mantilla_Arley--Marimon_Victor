import sys
sys.path.append("..")
from menus import *
from MODULO_CIUDADES.crud_ciudades import *


while True:
    menu_principal()
    opc = pedir_opc()
    if opc == 1:
        agregar_ciudad()
    elif opc == 2: 
        actualizar_ciudades()
    elif opc == 3:
        eliminar_ciudad()
    elif opc == 4:
        print("Buscar ciudad(Filtros)")
    elif opc == 0:
        print("Hasta luego")
        break