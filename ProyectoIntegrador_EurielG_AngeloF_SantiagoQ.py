#   ___  ___  ______  _____________________    _____  ____________________  ___   ___  ____  ___ 
#  / _ \/ _ \/ __ \ \/ / __/ ___/_  __/ __ \  /  _/ |/ /_  __/ __/ ___/ _ \/ _ | / _ \/ __ \/ _ \
# / ___/ , _/ /_/ /\  / _// /__  / / / /_/ / _/ //    / / / / _// (_ / , _/ __ |/ // / /_/ / , _/
#/_/  /_/|_|\____/ /_/___/\___/ /_/  \____/ /___/_/|_/ /_/ /___/\___/_/|_/_/ |_/____/\____/_/|_| 
#                      
# SISTEMA DE INVENTARIO: TIENDA DEPARTAMENTAL DE ELECTRONICOS
#                                                                          
# Pensamiento Computacional para la ingeniería
# Sergio Adán Flores Cantú
#
# --- EQUIPO 5 ---
# Santiago Quintana Moreno A01571222                                                                                      
# Euriel Gomez Tamez       A00838859
# Angelo Franco Baez       A00840411     


import time

logo = """
 _       _____    ____  ___________
| |     / /   |  / __ \/ ____/ ___/
| | /| / / /| | / /_/ / __/  \__ \ 
| |/ |/ / ___ |/ _, _/ /___ ___/ / 
|__/|__/_/  |_/_/ |_/_____//____/  
                                   
"""

print(logo)
print("Warehouse Arrival and Records, Inventory Evaluation, Sales Data, Sales Reports System")



def verificacionContrasenia():
    usuariosPermitidos = ["admin", "EurielGT", "AngeloFB", "SantiagoQM", "SergioF"]
    contraseniasPermitidas = ["admin", "EGT260106", "AFB291103", "SQM090503", "TC1028"]

    bloqueoSegundos = 5
    intentosMaximos = 3
    for intento in range(1, intentosMaximos + 1):
        usuarioIngresado = input(f"Ingrese su Usuario: ")
        contraseniaIngresada = input(f"Ingrese su Contraseña: ")
        if usuarioIngresado in usuariosPermitidos and contraseniaIngresada in contraseniasPermitidas:
            print("Login Correcto")
            return intento
        else:
            print(f"Usuario o contraseña equivocado. Intente de nuevo. Intentos restantes: {intentosMaximos - intento}.")

    print("Bloqueando el sistema.")
    time.sleep(bloqueoSegundos)
    return intentosMaximos
    
def menu():
    codigo = input("Ingrese su código: ")

    codigosDeAdmin = ["admin", "TC1028"]

    if codigo in codigosDeAdmin:
        print("--- MENU DE ADMIN ---")
        print("[ 1 ] Registrar ventas")
        print("[ 2 ] Registrar llegada de artículos al almacén")
        print("[ 3 ] Consultar datos del inventario")
        print("[ 4 ] Consultar datos de las ventas")
        print("[ 5 ] Mostrar reportes de ventas por vendedor o por artículo")

        opcionAEjecutar = int(input("Ingrese su selección:"))

        return opcionAEjecutar

    else:
        print("--- MENU DE EMPLEADO ---")
        print("[ 1 ] Registrar ventas")
        print("[ 2 ] Registrar llegada de artículos al almacén")
        print("[ 3 ] Consultar datos del inventario")

        opcionAEjecutar = int(input("Ingrese su selección:"))

        return opcionAEjecutar


def seleccionMenu():
    opcionAEjecutar = menu()

    if opcionAEjecutar == 1:
        print("1 ADMIN")
    elif opcionAEjecutar == 2:
        print("2 ADMIN")
    elif opcionAEjecutar == 3:
        print("3 ADMIN")
    elif opcionAEjecutar == 4:
        print("4 ADMIN")
    elif opcionAEjecutar == 5:
        print("5 ADMIN")
    else:
        print("Error admin")

    opcionAEjecutar = menu()

    if opcionAEjecutar == 1:
        print("1 EMPLEADO")
    elif opcionAEjecutar == 2:
        print("2 EMPLEADO")
    elif opcionAEjecutar == 3:
        print("3 EMPLEADO")
    else:
        print("Error empleado")
    
if __name__ == '__main__':
    verificacionContrasenia()
    seleccionMenu()










#A esta función aún le falta la opción de volver a intentar en caso de tener mal una entrada de usuario y contraseña. Además, no funciona el contador de intentos. 
#Quizá integrar una función donde se puedan añadir usuarios y sus contraseñas con manipulación de archivos. 
#Cuando falla, aún muestra el MENU, revisar eso. 
