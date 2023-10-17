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


#--------------------------------------------------------------------------------------- LOG IN -----------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------- LOG IN -----------------------------------------------------------------------------

#---------------------------------------------------------------------------------- REGISTRO DE VENTAS ----------------------------------------------------------------------





#---------------------------------------------------------------------------------- REGISTRO DE VENTAS ----------------------------------------------------------------------

#---------------------------------------------------------------------------------- GESTOR DE INVENTARIO --------------------------------------------------------------------
def agregarArticulo(inventario, contador, articulo, sku, cantidad):
    inventario.append([contador, articulo, sku, cantidad])

def guardarInventario(nombre_archivo, inventario):
    with open(nombre_archivo, 'w') as archivo:
        for item in inventario:
            archivo.write(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\n")

def gestorDeInventario():
    inventario = []  
    contador = 1

    while True:
        print("Opciones:")
        print("1. Agregar artículo al inventario")
        print("2. Mostrar inventario")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            articulo = input("Nombre del artículo: ")
            sku = input("SKU: ")
            cantidad = int(input("Cantidad: "))
            agregarArticulo(inventario, contador, articulo, sku, cantidad)
            contador += 1
        elif opcion == "2":
            print("Inventario:")
            for item in inventario:
                print(f"#: {item[0]}, Artículo: {item[1]}, SKU: {item[2]}, Cantidad: {item[3]}")
        elif opcion == "3":
            guardarInventario("Inventario.txt", inventario)
            print("Inventario guardado en 'Inventario.txt'. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
#---------------------------------------------------------------------------------- GESTOR DE INVENTARIO --------------------------------------------------------------------

#------------------------------------------------------------------------------------ DATOS DE VENTAS -----------------------------------------------------------------------





#------------------------------------------------------------------------------------ DATOS DE VENTAS -----------------------------------------------------------------------

#------------------------------------------------------------------------------ REPORTE DE VENTAS POR EMPLEADO --------------------------------------------------------------





#------------------------------------------------------------------------------ REPORTE DE VENTAS POR EMPLEADO --------------------------------------------------------------

#------------------------------------------------------------------------------------------ MENU ----------------------------------------------------------------------------
def menu():
    print("Espere para validación de credenciales de Administrador. En caso de ser empleado, ingrese: Empleado.")
    time.sleep(2)
    codigo = input("Ingrese su código de Administrador: ")

    codigosDeAdmin = ["admin", "TC1028"]

    if codigo in codigosDeAdmin:
        print("--- MENU DE ADMIN ---")
        print("[ 1 ] Registrar ventas")
        print("[ 2 ] Administración de Inventario.")
        print("[ 3 ] Consultar datos de las ventas")
        print("[ 4 ] Mostrar reportes de ventas por vendedor o por artículo")

        opcionAEjecutar = int(input("Ingrese su selección:"))

    else:
        print("--- MENU DE EMPLEADO ---")
        print("[ 1 ] Registrar ventas")
        print("[ 2 ] Administración de Inventario.")

        opcionAEjecutar = int(input("Ingrese su selección:"))

    return opcionAEjecutar
#------------------------------------------------------------------------------------------ MENU ----------------------------------------------------------------------------

#----------------------------------------------------------------------------------- EJECUCIÓN DEL MENU ---------------------------------------------------------------------
def seleccionMenu():
    opcionAEjecutar = menu()

    if "admin" or "TC1028" in codigosDeAdmin:
        if opcionAEjecutar == 1:
            print("--- REGISTRO DE VENTAS ---")
        elif opcionAEjecutar == 2:
            print("--- GESTOR DE INVENTARIO ---")
            gestorDeInventario()

        elif opcionAEjecutar == 3:
            print("--- DATOS DE VENTAS ---")
        elif opcionAEjecutar == 4:
            print("--- REPORTE DE VENTAS POR VENDEDOR O ARTICULO ---")
        else:
            print("Error admin")

    else:
        if opcionAEjecutar == 1:
            print("--- REGISTRO DE VENTAS ---")
        elif opcionAEjecutar == 2:
            print("--- ADMINISTRACIÓN DE INVENTARIO ---")
        else:
            print("Error empleado")
#----------------------------------------------------------------------------------- EJECUCIÓN DEL MENU ---------------------------------------------------------------------

#------------------------------------------------------------------------------------------ MAIN -----------------------------------------------------------------------------
if __name__ == '__main__':
    verificacionContrasenia()
    codigosDeAdmin = ["admin", "TC1028"]
    seleccionMenu()
#------------------------------------------------------------------------------------------ MAIN -----------------------------------------------------------------------------



