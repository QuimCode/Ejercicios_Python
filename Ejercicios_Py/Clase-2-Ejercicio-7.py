#----------------------------------------------------------------------------------------------------#

# Ejercicios Listas
# Quimey Alejo Fontan - Programacion - DIV B - Giovanni
# 2-
# La real academia española nos pide desarrollar un pequeño programa que contenta el
# diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
# algoritmo que nos permita el ingreso de una palabra en español y su traducción al
# ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
# palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
# esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
# debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
# inglés. Recordar validar los datos de forma correcta.

#----------------------------------------------------------------------------------------------------#

diccionaario_idiomas = []

while True:

    ingreso_español = input ("Ingrese las letras que conformaran la palabra en ESPAÑOL. Si ya no desea ingresar mas datos simplemente ingrese 'q'. ")
    if ingreso_español.lower() == "q":
        break

    if not ingreso_español.isalpha():
        print("Por favor, ingrese solo letras para la palabra en español. ")
        continue

#----------------------------------------------------------------------------------------------------#

    ingreso_ingles = input ("Ingrese las letras que conformaran la palabra en INGLES. ")

    if not ingreso_ingles.isalpha():
        print("Por favor, ingrese solo letras para la palabra en INGLES. ")
        continue

#----------------------------------------------------------------------------------------------------#

    indice = -1
    for i in range(len(diccionaario_idiomas)):   
        if diccionaario_idiomas[i][0] == ingreso_español:
            indice = i
            break

    if indice == -1:
        diccionaario_idiomas.append([ingreso_español, ingreso_ingles])
        print(f"Palabra agregada: {ingreso_español} -> {ingreso_ingles}")
    else:
        print(f"La palabra '{ingreso_español}' ya existe en el diccionario. Índice: {indice}")

#----------------------------------------------------------------------------------------------------#

print("Listado de palabras ingresadas:")
for palabra in diccionaario_idiomas:
    print(f"{palabra[0]} -> {palabra[1]}")