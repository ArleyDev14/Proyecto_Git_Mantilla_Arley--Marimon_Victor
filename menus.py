def menu_principal():
    print("--------------------------")
    print("Ingresa [1] para --> Registrar una ciudad")
    print("Ingresa [1] para --> Actualizar datos de una ciudad")
    print("Ingresa [1] para --> Eliminar ciudad")
    print("Ingresa [1] para --> Buscar ciudad(Filtros)")
    print("--------------------------")

def pedir_opc():
    opc = 0
    try:
        opc = int(input("Ingresa tu elección: "))
        return opc
    except Exception:
        print("Valor invalido")
        return 0