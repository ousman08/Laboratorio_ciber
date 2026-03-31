# Ejercicios:
# 1. Escribe un programa que solicite un número y gestione el error si se ingresa
# texto.
# 2. Crea un script que intente abrir un archivo que no existe y maneje el error
# mostrando un mensaje personalizado.


print("1. Escribe un programa que solicite un número y gestione el error si se ingresa texto.")
try:
   num = int(input("Escribe un numero: "))
   print(f"Tu numero es: {num}")
   
except ValueError:
    print("Error, no has escrito un numero")
    
    
print("2. Crea un script que intente abrir un archivo que no existe y maneje el error mostrando un mensaje personalizado.")