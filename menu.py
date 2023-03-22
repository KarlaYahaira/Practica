import Funciones


def mostrar_menu():
    print("")
    print("Varias funciones")
    print("1. Calcular la serie fibonachi")
    print("2. Calcular la cantidad, suma y promedio de numeros pares e impares")
    print("3. Buscar animal ingresando los datos")
    print("4. Salir")
    opcion = int(input("Seleccione la opción:   "))
    Funciones.clear()
    return opcion



def llamadas_varias(opc):

    final = 0
    while opc != 4:
        if opc == 1:
            Funciones.fibona()
            Funciones.pausa()
            break
        if opc == 2:
            Funciones.par_impar()
            Funciones.pausa()
            break
        if opc == 3:
            Funciones.buscar_animal()
            Funciones.pausa()
            break
        if opc == 4:
            print("Saliendo del programa")
            Funciones.pausa()

    return final




