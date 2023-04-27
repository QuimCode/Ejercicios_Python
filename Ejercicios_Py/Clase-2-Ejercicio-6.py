#----------------------------------------------------------------------------------------------------#

# Ejercicios Listas
# Quimey Alejo Fontan - Programacion - DIV B - Giovanni
# 1-
# Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
# autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
# marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
# listas primero, y despues usando listas y comparar la composición del código.

#----------------------------------------------------------------------------------------------------#

# marca = ""
# año = 0
# precio = 0.0

# while True:
#     marca = input("Ingrese la marca del auto (o escriba 'salir'):")
#     if marca.lower() == 'salir':
#         break

#     año = int(input("Ingrese el año del modelo del auto:"))

#     precio = float(input("Ingrese el preico del auto:"))

#     print("Marca: ", marca)
#     print("Año-Modelo: ", año)
#     print("Precio: ", precio)

#----------------------------------------------------------------------------------------------------#

print("Sistema de Control de Stock de Autos")
autos_ingresados = []
while True:
        marca = input("Ingrese la marca del auto: ")
        año = input("Ingrese el año del modelo: ")
        precio = input("Ingrese el precio del auto: ")
        auto = {
            "marca": marca,
            "año": año,
            "precio": precio
        }
        autos_ingresados.append(auto)
        continuar = input("Desea ingresar otro auto? (si/no): ")
        if continuar.lower() == "no":
            break

print("Listado de autos ingresados:")
for auto in autos_ingresados:
    print("-------------")
    print("Marca:", auto["marca"])
    print("Año:", auto["año"])
    print("Precio:", auto["precio"])
    print("-------------")

#----------------------------------------------------------------------------------------------------#