import sys
sys.path.append("..")
from menus import *

while True:
    menu_principal()
    opc = pedir_opc()
    if opc == 1:
        print("Registrar una ciudad")
    elif opc == 2: 
        print("Actualizar datos de una ciudad")
    elif opc == 3:
        print("Eliminar ciudad")
    elif opc == 4:
        print("Buscar ciudad(Filtros)")