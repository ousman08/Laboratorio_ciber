# Ejercicios:1. Crea una lista con cinco direcciones IP. Luego, recorre la lista e imprime cada IP
# en pantalla.
# 2. Define un diccionario con nombres de usuario como claves y estados de acceso
# (True/False) como valores. Escribe una función que muestre sólo los usuarios
# activos.


print("Crea una lista con cinco direcciones IP. Luego, recorre la lista e imprime cada IP en pantalla.")

ips = ['190.000.000.000', '190.190.000.000', '192.200.150.000','192.168.1.1','192.168.21.1']
    
for ip in ips:
        
    print(ip)  
print()


print('Define un diccionario con nombres de usuario como claves y estados de acceso (True/False) como valores. Escribe una función que muestre sólo los usuarios activos.')


usuario = {
    "usuario1": {"usuario": "ana", "activo": True},
    "usuario2": {"usuario": "leni", "activo": False},
    "usuario3": {"usuario": "maha", "activo": True},
    "usuario4": {"usuario": "morad", "activo": False},
    "usuario5": {"usuario": "pera", "activo": True},    
}

def diccionario():
    
    for clave, estado in usuario.items():
        
        if estado["activo"]:
        
            print(estado)        
diccionario()
