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
    intento = 1

    while intento <= intentosMaximos:
        usuarioIngresado = input("Ingrese su Usuario: ")
        contraseniaIngresada = input("Ingrese su Contraseña: ")

        if usuarioIngresado in usuariosPermitidos and contraseniaIngresada in contraseniasPermitidas:
            print("Login Correcto")
            return intento

        print(f"Usuario o contraseña equivocado. Intente de nuevo. Intentos restantes: {intentosMaximos - intento}.")
        intento += 1

    print("Bloqueando el sistema.")
    time.sleep(bloqueoSegundos)
    return None
#--------------------------------------------------------------------------------------- LOG IN -----------------------------------------------------------------------------

#---------------------------------------------------------------------------------- REGISTRO DE VENTAS ----------------------------------------------------------------------
def registrarVenta():
    nombre_vendedor = input("Ingrese el nombre del vendedor: ")
    nombre_articulo = input("Ingrese el nombre del artículo: ")
    sku = input("Ingrese el SKU: ")
    cantidad = int(input("Ingrese la cantidad de artículos: "))
    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    precio_por_unidad = float(input("Ingrese el precio por unidad: "))
    
    venta = [nombre_vendedor, nombre_articulo, sku, cantidad, fecha, precio_por_unidad]
    
    with open("registro_ventas.txt", "a") as archivo_ventas:
        archivo_ventas.write(f"{'Vendedor'.ljust(15)}{'Artículo'.center(30)}{'SKU'.center(15)}{'Cantidad'.rjust(10)}{'Fecha'.center(15)}{'Precio por Unidad'.rjust(15)}\n")
        archivo_ventas.write(f"{venta[0].ljust(15)}{venta[1].center(30)}{venta[2].center(15)}{str(venta[3]).rjust(10)}{venta[4].center(15)}{str(venta[5]).rjust(15)}\n")
    
    print("Venta registrada exitosamente")
#---------------------------------------------------------------------------------- REGISTRO DE VENTAS ----------------------------------------------------------------------

#---------------------------------------------------------------------------------- GESTOR DE INVENTARIO --------------------------------------------------------------------
def agregarArticulo(inventario, contador, articulo, sku, cantidad):
    inventario.append([contador, articulo, sku, cantidad])

def guardarInventario(nombre_archivo, inventario):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Inventario:\n")
        archivo.write(f"{'#'.ljust(10)}{'Artículo'.center(30)}{'SKU'.center(15)}{'Cantidad'.rjust(20)}\n")
        for item in inventario:
            archivo.write(f"{str(item[0]).ljust(10)}{item[1].center(30)}{item[2].center(15)}{str(item[3]).rjust(20)}\n")

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
            print(f"{'#'.ljust(10)}{'Artículo'.center(30)}{'SKU'.center(15)}{'Cantidad'.rjust(20)}")
            for item in inventario:
                print(f"{str(item[0]).ljust(10)}{item[1].center(30)}{item[2].center(15)}{str(item[3]).rjust(20)}")
        elif opcion == "3":
            guardarInventario("Inventario.txt", inventario)
            print("Inventario guardado en 'Inventario.txt'. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
#---------------------------------------------------------------------------------- GESTOR DE INVENTARIO --------------------------------------------------------------------

#------------------------------------------------------------------------------------ DATOS DE VENTAS -----------------------------------------------------------------------
def mostrarVentas():
    with open("registro_ventas.txt", "r") as archivo_ventas:
        header = archivo_ventas.readline()  
        print(header.strip()) 
        
        for linea in archivo_ventas:
            datos = linea.strip().split(',')
            if len(datos) >= 6:
                print(f"{datos[0].ljust(15)}{datos[1].center(30)}{datos[2].center(15)}{datos[3].rjust(10)}{datos[4].center(15)}{datos[5].rjust(15)}")
            else:
                print("Línea de datos incompleta:", linea)
#------------------------------------------------------------------------------------ DATOS DE VENTAS -----------------------------------------------------------------------

#------------------------------------------------------------------------------ REPORTE DE VENTAS POR EMPLEADO --------------------------------------------------------------
def crearReporte():
    nombre_vendedor = input("Por favor, ingresa el nombre del vendedor: ")
    fecha = input("Ingresa la fecha del reporte: ")
    articulo = input("Ingresa el artículo: ")

    with open("Reporte.txt", "w") as archivo:
        archivo.write(f"Información del Reporte:\n")
        archivo.write(f"Nombre del vendedor: {nombre_vendedor}\n")
        archivo.write(f"Fecha: {fecha}\n")
        archivo.write(f"Artículo: {articulo}\n")

    print("El archivo Reporte.txt se ha creado exitosamente con la información proporcionada.")
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
    while True:
        opcionAEjecutar = menu()

        if "admin" or "TC1028" in codigosDeAdmin:
            if opcionAEjecutar == 1:
                print("--- REGISTRO DE VENTAS ---")
                registrarVenta()

            elif opcionAEjecutar == 2:
                print("--- GESTOR DE INVENTARIO ---")
                gestorDeInventario()

            elif opcionAEjecutar == 3:
                print("--- DATOS DE VENTAS ---")
                mostrarVentas()

            elif opcionAEjecutar == 4:
                print("--- REPORTE DE VENTAS POR VENDEDOR ---")
                crearReporte()

            else:
                print("Ha ocurrido un error. Intente de nuevo.")

        else:
            if opcionAEjecutar == 1:
                print("--- REGISTRO DE VENTAS ---")
            elif opcionAEjecutar == 2:
                print("--- ADMINISTRACIÓN DE INVENTARIO ---")
            else:
                print("Ha ocurrido un error. Intente de nuevo.")

        seguir = input("¿Desea realizar otra acción? (s/n): ")
        if seguir.lower() != 's':
            break

#----------------------------------------------------------------------------------- EJECUCIÓN DEL MENU ---------------------------------------------------------------------

#------------------------------------------------------------------------------------------ MAIN -----------------------------------------------------------------------------
if __name__ == '__main__':
    verificacionContrasenia()
    codigosDeAdmin = ["admin", "TC1028"]
    seleccionMenu()
#------------------------------------------------------------------------------------------ MAIN -----------------------------------------------------------------------------