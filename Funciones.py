import os, time
def clear():
    os.system('cls'if os.name == 'nt' else 'clear')
    #limpia la consola

def pausa():
    os.system("pause")
    #El usuario debe presionar una tecla para continuar

def espera():
    time.sleep(5)
    #Genera una espera de 5 segundos

def fibona():
    x = 0
    y = 1
    z = 0

    n = int(input("Ingrese un numero mayor a 1:  "))
    while True:
        if n > 1:
            break

    for x in range(0, n):
        z = x + y
        print(f"{z}", end=" ")
        x = y
        y = z
        print("")


def par_impar():

    #inicializar variables
    cp = 0
    sumapar = 0
    promediopar = 0
    cimpar = 0
    suma_impar = 0
    promedio_impar = 0


    #Entrada de datos número inicial y número final donde va a determinar la cantidad de números pares
    # e impares, asi como la suma de ellos y el promedio

    numero_inicial = int(input("Digite el valor inicial:  "))
    numero_final = int(input("Digite el valor final:  "))
    for i in range(numero_inicial, numero_final + 1):
        if i % 2 == 0:
            cp = cp + 1
            sumapar = sumapar + i
            promediopar = sumapar / cp

    for i in range(numero_inicial, numero_final + 1):
        if i % 2 != 0:
            cimpar = cimpar + 1
            suma_impar = suma_impar + i
            promedio_impar = suma_impar / cimpar

    print("La cantidad de numeros pares son:  ")
    print(cp)
    print("La suma de los numeros pares es: ")
    print(sumapar)
    print("El promedio de los numeros pares es:  ")
    print(promediopar)

    print("La cantidad de numeros impares son:  ")
    print(cimpar)
    print("La suma de los numeros impares es: ")
    print(suma_impar)
    print("El promedio de los numeros impares es:  ")
    print(promedio_impar)

def buscar_animal():

    #inicializar vector
    animal = []

    # Entradas
    print("Ingresar la cantidad de animales: ")
    tamanimal = int(input())
    print("Ingrese los nombres de los animales:")

    for x in range(tamanimal):
        elemento = input("Ingrese el nombre del animal{}: ".format(x + 1))
        animal.append(elemento)

    print("Digite que animal desea buscar:")
    nombreAnimal = input()
    print("El animal tiene como vecino a:")
    print("------------------------------")

    for x in range(tamanimal):
        if animal[x] == nombreAnimal:

            if x == 0:
                # Como es Primero: No tiene vecino Izquierdo
                # #Imprimir solo el derecho
                print(animal[x+1])

            elif x == tamanimal-1:
                #Como es Ultimo: No tiene vecino Derecho
                #Imprimir solo el Izquierdo
                print(animal[x-1])

            else:
                #Imprimir Izquierda y derecha
                print(animal[x-1])
                print(animal[x+1])