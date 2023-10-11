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

time.sleep(1)

usuariosPermitidos = ["admin", "EurielGT", "AngeloFB", "SantiagoQM", "SergioF"]
pinesPermitidos = ["admin", "EGT260106", "AFB291103", "SQM090503", "TC1028"]
intentosMaximos = 3
    

def verificacionContrasenia(pinesPermitidos):
    for intento in range(1, intentosMaximos + 1):
        pinIngresado = input(f"Intento {intento}: Ingrese el PIN: ")

        if pinIngresado == pinesPermitidos:
            print("Login Correcto")
            break 
        else:
            print("PIN incorrecto")

    else:
        print("Llamando a la policía")

"""
def verificar_usuario_contraseña():
    usuarios = {
        "usuario1": "contraseña1",
        "usuario2": "contraseña2",
        "usuario3": "contraseña3"
    }
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    for user, password in usuarios.items():
        if usuario == user and contraseña == password:
            print("Acceso concedido.")
            break
    else:
        print("Usuario o contraseña incorrectos.")

verificar_usuario_contraseña()
"""




print("---- MENU ---- \n")

print("[1] = Cuenta números.")
print("[2] = Suma de N números consecutivos.")
print("[3] = Lista de precios.")
print("[4] = Promedio Sencillo.")
print("[5] = Promedio con Desición.")
1