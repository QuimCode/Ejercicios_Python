#Comentario Una sola Linea

'''
Comentarios
Multi-Linea
'''

nombre = "Quimey"
edad = 23

if nombre == "Quimey" and edad > 20:
    print("Gracias por utilizar nuestro sistema")
else:
    if nombre == "Maria":
        print("Bienvenido Maria")
    else:
        if nombre == "Jose":
            print("Bienvenido Jose")
        else:
            print("Usted no se llama ni Juan, ni Maria, ni Jose")


color = "rojo"

if color == "azul":
    print("Es azul")
if color == "verde":
    print("Es verde")
if color == "amarillo":
    print("Es amarillo")
if color == "rojo":
    print("Es rojo")

if color != "azul" and color != "verde" and color != "amarillo" and color != "rojo":
    print("Es otro color")


if color == "azul":
    print("Es azul")
else:
    if color == "verde":
        print("Es verde")
    else:
        if color == "amarillo":
            print("Es amarillo")
        else:
            if color == "rojo":
                print("Es rojo")
            else:
                print("Es otro color")

if color == "azul":
    print("Es Azul")
elif color == "verde":
    print("verde")
elif color == "amarillo":
    print("amarillo")
elif color == "rojo":
    print("rojo")
else:
    print("Es otro color")

acumulador = 0
seguir = True

while seguir:
    numero = int(input("Ingrese un numero"))
    acumulador += numero

    seguir = input("Desea Continuar ?")
    if seguir == "si":
        seguir = True

    #"forma de DoWhile"
    # seguir = input("Desea Continuar ?")
    # if seguir != "si":
    #     break

print(f"Acumulado: {acumulador}")

lista_numeros = list(range(5))
print(lista_numeros)

lista_numeros2 = list(range(5, 25, 2))
print(lista_numeros2)

acumulador = 0

for Q in range(5):
    numero = int(input("Ingrese un numero"))
    acumulador =+ numero

print(f"Acumulado: {acumulador}")

lista_nombres = ["Luis", "Federico", "Micaela", "Silvina", "Nicolas"]
for nombre in lista_nombres:#foreach
    print(nombre)


    color = "azul"
    match color:
        case "azul":
            print("Es azul")
        case "verde":
            print("Es verde")
        case "amarillo":
            print("Es amarillo")
        case "rojo":
            print("Es rojo")
        case _:
            print("Es otro color")