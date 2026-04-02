# Ejercicios:
# 1. Escribe un programa que cree un archivo y escriba tres líneas de texto
# relacionadas con eventos de seguridad.
# 2. Crea un programa que lea un archivo de texto y cuente cuántas veces aparece la
# palabra "error".

print("1. Escribe un programa que cree un archivo y escriba tres líneas de texto relacionadas con eventos de seguridad.")

#Abrimos o creamos el archivo "eventos_seguridad.txt"
# El modulo "w" significa escritura "write"
#si el archivo ya existe, se sobrescribe
with open("eventos_seguridad.txt", "w") as archivo:
   
   #Escribimos la primera línea en el archivo
   #n sirve para hacer un salto de línea
   archivo.write("Intento de acceso no autorizado detectado,\n")
   
   #segunda linea de texto relacionado con un ataque
   archivo.write("se a producido un ataque de fuerza bruta en el servidor")
   
   #Tercera linea indicando una acción de seguridad
   archivo.write("actualizaciond de seguridad aplicada correctamente.\n")

print("Archivo creado y datos escritos correctamente.")