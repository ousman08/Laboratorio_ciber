# Ejercicios:
# 1. Escribe un programa que solicite una contraseña al usuario y verifique si
# coincide con una clave predefinida.
# 2. Diseña un programa que imprima los números del 1 al 10, pero que indique
# cuáles son pares y cuáles impares.

def Ejercicio1():
    print("1. Escribe un programa que solicite una contraseña al usuario y verifique si coincide con una clave predefinida.")
    
    import getpass
    
    # Bases de datos de 2 usuarios
    database = {"user1": "12345", "user2": "6789"}
    
    # Pedir nombre usuario
    username = input("Introduce usuario: ")
    
    # Comprobar usuario en base de datos
    if username in database:
        #Pedir contraseña
        password = getpass.getpass("contraseña: ")
        
        #Pedir contraseña hasta que sea valida
        while password != database[username]:
            password = getpass.getpass("Contraseña no válida. Intente de nuevo ")
        print("Username verificado")
    else:
        print("Username no encontrado")
        
        
    """    #Comprobar contraseña
        if password == database[username]:
            print("Username verificado")
        else:
            print("Contraseña no valida")
    else:
        print("usuario no encontrado")"""
       
Ejercicio1()
print()

print("2. Diseña un programa que imprima los números del 1 al 10, pero que indique cuáles son pares y cuáles impares.")

# creo un bucle for, empieza 1 saliendo cuando llega 10.
# usanfo el operador de resto(%) para comprobar si es par o impar
for i in range(1, 11):
    if i % 2 == 0:       
        print(i, "es par")
    else:
        print(i,"es impar")