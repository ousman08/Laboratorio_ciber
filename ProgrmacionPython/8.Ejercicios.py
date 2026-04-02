# Ejercicios:
# 1. Usa el módulo datetime para mostrar la hora exacta de ejecución del script.
# 2. Utiliza re para detectar y extraer todas las IPs presentes en un texto simulado de
# # log.

print("1. Usa el módulo datetime para mostrar la hora exacta de ejecución del script.")


# Importamos el modulo datetime
from datetime import datetime

# obtenemos la fecha actual del sistema
ahora = datetime.now()

# con strftime("%H:%M:%S") mostramos solo la hora exacta de ejecución
print("Hora de ejecución:", ahora.strftime("%H:%M:%S"))


print("2. Utiliza re para detectar y extraer todas las IPs presentes en un texto simulado de log.")


# Importamos el modulo de expresiones regulares

import re

# Simulamos un log con varios dirrecciones IP
log = """
Acceso perimitido desde 192.168.1.1
Intento fallido desde 10.0.0.45
Ataque detectado desde 172.16.0.3
Usuario conectado desde 172.116.1.1
"""

#Expresiónes regulares para detectar direcciones IP
patron_ip = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

#Buscamos todas las IPs en el texto
ips_encontradas = re.findall(patron_ip, log)

#Mostramos las IPs encontradas
print("IPs encontradas:")
for ip in ips_encontradas:
   print(ip)
