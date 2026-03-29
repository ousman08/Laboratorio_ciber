# Ejercicios:
# 1. Escribe una función que reciba un nombre y devuelva un saludo personalizado.
# 2. Crea una función que reciba una lista de números y devuelva el promedio de
# esos números.


print("1. Escribe una función que reciba un nombre y devuelva un saludo personalizado.")

def saludo(nombre):
    
    #la funcion solo se encarga de armar el saludo
    return f"Hola que tal, {nombre}"

#1. Pedimos el datos fuera de la funcion
usuario = input("Escribe tu nombre: ")

#2. llamamos a la funcion y guardamos el resultado
mensaje = saludo(usuario)

#3. Mostramos el resultado
print(mensaje)



print("2. Crea una función que reciba una lista de números y devuelva el promedio de esos números.")