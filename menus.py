def menu_principal():
    print("--------------------------")
    print("Ingresa [1] para --> Registrar una ciudad")
    print("Ingresa [2] para --> Actualizar datos de una ciudad")
    print("Ingresa [3] para --> Eliminar ciudad")
    print("Ingresa [4] para --> Buscar ciudad(Filtros)")
    print("Ingresa [5] para --> Ver todas las ciudades")
    print("Ingresa [0] para --> Salir / Cerrar")
    print("--------------------------")

def pedir_opc():
    opc = 0
    try:
        opc = int(input("Ingresa tu elección: "))
        return opc
    except Exception:
        print("Valor invalido")
        return 0