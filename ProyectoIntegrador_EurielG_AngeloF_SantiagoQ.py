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

time.sleep(1.5)


bloqueoSegundos = 5
intentosMaximos = 3
    

def verificacionContrasenia(usuariosPermitidos, contraseniasPermitidas):
    for intento in range(1, intentosMaximos + 1):
        if usuarioIngresado in usuariosPermitidos and contraseniaIngresada in contraseniasPermitidas:
            print("Login Correcto")
            return intento
        else:
            print(f"Usuario o contraseña equivocado. Intente de nuevo. Intentos restantes: {intentosMaximos - intento}.")
    
    print("Bloqueando el sistema.")
    time.sleep(bloqueoSegundos)
    return intentosMaximos

usuariosPermitidos = ["admin", "EurielGT", "AngeloFB", "SantiagoQM", "SergioF"]
contraseniasPermitidas = ["admin", "EGT260106", "AFB291103", "SQM090503", "TC1028"]


usuarioIngresado = input(f"Ingrese su Usuario: ")
contraseniaIngresada = input(f"Ingrese su Contraseña: ")
intentos = verificacionContrasenia(usuariosPermitidos, contraseniasPermitidas)
print(f"Número total de intentos {intentos}.")




#A esta función aún le falta la opción de volver a intentar en caso de tener mal una entrada de usuario y contraseña. Además, no funciona el contador de intentos. 
#Quizá integrar una función donde se puedan añadir usuarios y sus contraseñas con manipulación de archivos. 
#Cuando falla, aún muestra el MENU, revisar eso. 

print("---- MENU ---- \n")

print("[1] = Cuenta números.")
print("[2] = Suma de N números consecutivos.")
print("[3] = Lista de precios.")
print("[4] = Promedio Sencillo.")
print("[5] = Promedio con Desición.")
