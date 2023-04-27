# Quimey Alejo Fontan - Programacion - DIV B - Giovanni
# Ejercicio 4
# La división de alimentos está trabajando en un pequeño software para cargar las
# compras de ingredientes para la cocina de Industrias Wayne.
# Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
# para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
# de ingredientes.
# Se registra por cada compra:
# 1. PESO: (entre 10 y 100 kilos)
# 2. PRECIO POR KILO: (mayor a 0 [cero]).
# 3. TIPO VARIEDAD: (vegetal, animal, mezcla).
# Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
# descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
# de descuento sobre el precio bruto.
# Se desea saber:
# A. El importe total a pagar, BRUTO sin descuento.
# B. El importe total a pagar con descuento (Solo si corresponde).
# C. Informar el tipo de alimento más caro.

kilos_totales = 0
importe_bruto_total = 0 
importe_descuento = 0
tipo_alimento_mas_caro = ""
precio_mas_caro = 0
importe_total = 0

lista_numero = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in lista_numero:
    print("Compra numero #", i + 1)

    peso = int(input("Ingrese el peso de los objetos a comprar, entre 10 a 100 Kg. "))
    while peso <= 10 and peso >= 100:
        peso = int(input("Error, Ingrese el peso de los objetos a comprar, entre 10 a 100 Kg. "))

    precio = float(input("Ingrese el precio del objeto a comprar."))
    while precio <= 0:
        precio = float(input("Ingrese el precio del objeto a comprar."))

    producto = input("Ingrese el tipo de producto que desea comprar, vegetal, animal, mezcla. ")
    while producto != "vegetal" and producto != "animal" and producto != "mezcla":
        producto = input("Error ingrese un valor asignado (vegetal/animal/mezcla)")

    importe_bruto_total += peso * precio
    kilos_totales += peso

if precio > precio_mas_caro:
    precio_mas_caro = precio
    tipo_alimento_mas_caro = producto

if kilos_totales > 100 and kilos_totales <= 300:
    importe_descuento = importe_bruto_total * 0.15
elif kilos_totales > 300:
    importe_descuento = importe_bruto_total * 0.25

    importe_total = importe_bruto_total - importe_descuento

    print("A. Importe total a pagar (BRUTO): $", importe_bruto_total)
    if importe_descuento > 0:
        print("B. Importe total a pagar con descuento: $", importe_total)
    if tipo_alimento_mas_caro != "":
        print("C. Tipo de alimento más caro: ", tipo_alimento_mas_caro)