# Ejercicios:
# 1. Crea un script que defina variables de tipo entero, decimal, cadena y booleano.
# Imprime todas las variables.
# 2. Escribe un programa que reciba dos números por teclado, los sume y muestre el
# # resultado.


def ejercicio1():
    print("1. Crea un script que defina variables de tipo entero, decimal, cadena y booleano. Imprime todas las variables.")
    
    #defino la lista de tipos
    entero = 1997
    decimal = 1.14
    cadena = 'hola hola'
    booleano = True | False
    
    #guardo la lista
    lista = (entero, decimal, cadena, booleano)
    
    #creo bucle for, traendo la lista, guardando lo en variable i,
    for i in lista:
    # funcion: type() -> para ver la 'clase', dentro de i
        tipo = type(i)
    # imprimiendo i, type
        print('la definicion de ', i, 'es ', tipo)
    
ejercicio1()
print()

"""
ejercicio1() para imprimir
tengo dos opciones
shift + 2, 3 veces
    envolcerlo en def"""
    
def ejercicio2():
    print('2. Escribe un programa que reciba dos números por teclado, los sume y muestre el resultado.')
    
#bucle while
    while True:
        try:
            numero1 = int(input("Dime el primero número: "))
            # si es no numero break para error 
            break
        except ValueError:
            print("Error 400, error escribe un numero porfavor")
            print("Intentalo de nuevo ")
            
    while True:
        try:
            numero2 = int(input("Dime el segundo número: "))
            break
        except ValueError:
            print("Error 400, error escribe un numero porfavor")
            print("Intentalo de nuevo")
            
    print(f"La suma de {numero1} + {numero2} =", numero1 + numero2)
    
ejercicio2()  
