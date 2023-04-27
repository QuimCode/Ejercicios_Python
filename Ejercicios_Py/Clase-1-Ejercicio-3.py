# #Quimey Alejo Fontan - Programacion - DIV B - Giovanni
# Ejercicio 03
# Es la gala final de Gran Hermano y la producción nos pide un programa para contar
# los votos de los televidentes y saber cuál será el participante que ganará el juego.
# Los participantes finalistas son: Nacho, Julieta y Marcos.
# El televidente debe ingresar:
# ● Nombre del votante
# ● Edad del votante (debe ser mayor a 13)
# ● Género del votante (masculino, femenino, otro)
# ● El nombre del participante a quien le dará el voto positivo.
# No se sabe cuántos votos entrarán durante la gala.
# Se debe informar al usuario:
# A. El promedio de edad de las votantes de género femenino
# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
# Nacho o Julieta.
# C. Nombre del votante más joven que votó a Nacho.
# D. Nombre de cada participante y porcentaje de los votos qué recibió.
# E. El nombre del participante que ganó el reality (El que tiene más votos)

total_de_votos = 0
contador_para_nacho = 0
contador_para_julieta = 0
contador_para_marcos = 0
contador_femenino = 0
acumulador_edad_femenino = 0
primer_dato_de_votante = False
edad_votante_mas_joven_nacho = 999
nombre_del_votante_mas_joven = ""
contador_voto_25_40_masculino = 0
edad = 0

while True:
    nombre = input("Ingrese su nombre")
    print(f"Su nombre es {nombre}")

    edad = int(input("Ingrese su edad (Debe ser mayor de 13 años)")) 
    while edad <= 13:
        edad = int(input("Ingrese su edad (Debe ser mayor de 13 años)")) 

    participante = input("Ingrese el nombre de la persona a la que va a votar (Nacho, Julieta y Marcos)")
    if participante.lower() == "nacho":
        contador_para_nacho += 1
        if edad >= 13:
            if edad < edad_votante_mas_joven_nacho:
                primer_dato_de_votante = True
                edad_votante_mas_joven_nacho = edad
                nombre_del_votante_mas_joven = nombre
    elif participante.lower() == "julieta":
        contador_para_julieta += 1
    elif participante.lower() == "marcos":
        contador_para_marcos += 1
    else:
        print("Participante invalido. El voto no se contará.")

    genero = input("Ingrese el genero del votante(Masculino,Femenino,Otro)")
    if genero.lower() == "femenino":
        contador_femenino += 1
        acumulador_edad_femenino += edad
    elif genero.lower() == "masculino":
        if edad >= 25 and edad <= 40:
            if participante.lower() == "nacho" or participante.lower() == "julieta":
                contador_voto_25_40_masculino += 1

    total_de_votos += 1
    entrada = input("Ingrese si desea continuar 'Si/No'")
    if entrada.lower() == "no":
        break

if contador_femenino > 0:
    promedio_edad_femenino = acumulador_edad_femenino / contador_femenino
    print(f"El promedio de edad de los votantes de genero femenino es ... {promedio_edad_femenino}")
else:
    print("No hubo votos de genero femenino")

print(f"La cantidad de personas de genero masculino de 25 a 40 años que votaron a Nacho o Julieta es {contador_voto_25_40_masculino}")


if contador_para_nacho > 0:
    porcentaje_votos_nacho = contador_para_nacho/total_de_votos * 100
print(f"El promedio de votos para Nacho es de ... {porcentaje_votos_nacho}")
if contador_para_marcos > 0:
    porcentaje_votos_marcos = contador_para_marcos/total_de_votos * 100
print(f"El promedio de votos para Marcos es de ... {porcentaje_votos_marcos}")
if contador_para_julieta > 0:
    porcentaje_votos_julieta = contador_para_julieta/total_de_votos * 100
print(f"El promedio de votos para Julieta es de ... {porcentaje_votos_julieta}")

if contador_para_nacho > 0:
    if contador_para_nacho > contador_para_julieta and contador_para_nacho > contador_para_marcos:
        print(f"El ganador del sertamen es Nacho con un total de {contador_para_nacho} votos")

if contador_para_marcos > 0:
    if contador_para_marcos > contador_para_julieta and contador_para_marcos > contador_para_nacho:
        print(f"El ganador del sertamen es Marcos con un total de {contador_para_marcos} votos")

if contador_para_julieta > 0:
    if contador_para_julieta > contador_para_nacho and contador_para_julieta > contador_para_marcos:
        print(f"El ganador del sertamen es Julieta con un total de {contador_para_julieta} votos")
