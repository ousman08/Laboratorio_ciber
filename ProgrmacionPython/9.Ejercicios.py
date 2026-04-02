# Ejercicios:
# 1. Escribe un programa que solicite un número y gestione el error si se ingresa
# texto.
# 2. Crea un script que intente abrir un archivo que no existe y maneje el error
# mostrando un mensaje personalizado.

"""
print("1. Escribe un programa que solicite un número y gestione el error si se ingresa texto.")
try:
   num = int(input("Escribe un numero: "))
   print(f"Tu numero es: {num}")
   
except ValueError:
    print("Error, no has escrito un numero")
    
    
print("2. Crea un script que intente abrir un archivo que no existe y maneje el error mostrando un mensaje personalizado.")
"""

try:
    # Intentemos abrir un archivo que no existe
    with open("archivo_falso.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
        
except FileNotFoundError:
    #Mensaje si el archivo no existe
    print("Error: No existe.")
    
except exception as e:
    #captura cualquier otro error
    print(f"Error inesperado: {e}")
    
finally:
    #Este bloque siempre se ejecuta
    print("Progrma finalizado")