#----------------------------------------------------------------------------------------------------#

# Ejercicios Listas
# Quimey Alejo Fontan - Programacion - DIV B - Giovanni
# 3-
# Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
# de memoria es la que mas ocurrencias tiene dentro de esa lista.

#----------------------------------------------------------------------------------------------------#

ingreso_numeral = []

while True:

    ingreso = input ("Ingrese los numeros que desee. Si ya no desea ingresar mas datos simplemente ingrese 'q'. ")
    if ingreso.lower() == "q":
        break

    if not ingreso.isdigit():
        print("Por favor, ingrese solo numeros para el ingreso de datos. ")
        continue

    ingreso_numeral.append(int(ingreso))

    ingresos_unicos = set(ingreso_numeral)
    ingresos_que_se_repiten = []
    for ingresos_Q in ingresos_unicos:
        if ingreso_numeral.count(ingresos_Q) > 1:
            ingresos_que_se_repiten.append(ingresos_Q)

#----------------------------------------------------------------------------------------------------#

if len(ingresos_que_se_repiten) > 0:
    print("Los siguientes elementos se repiten en la lista:")
    for ingresos_Q in ingresos_que_se_repiten:
        print(ingresos_Q)
else:
    print("No se encontraron elementos que se repitan en la lista.")