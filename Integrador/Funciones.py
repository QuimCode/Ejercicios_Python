#----------------------------------------------------------------------------------------------------#

# Quimey Alejo Fontan - Programacion - DIV B - Giovanni - FUNCIONES/DESAFIO-01
# Desafio Stark

#------------------------------------------------/EXPORTACIONES/----------------------------------------#

from data_stark import lista_personajes 

#------------------------------------------------/FUNCIONES-#01/---------------------------------------------#

def nombres_masculino():
    print("\n----------------- \nNombres de superhéroes Masculino:")
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            print(personaje["nombre"])

def nombres_femenino():
    print("\n----------------- \nNombres de superheroes Femeninos:")
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            print(personaje["nombre"])

def max_altura_masculino(imprimir_altura=True):
    max_altura = None
    max_nombre_m = None
    
    chekpoint_max_altura = False
    
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            altura = round(float(personaje["altura"]))
            if max_altura is None or altura > max_altura:
                max_altura = altura
                max_nombre_m = personaje["nombre"]
                chekpoint_max_altura = True

    if chekpoint_max_altura:
        if imprimir_altura:
            print(f"\n----------------- \nSuperheroe mas alto: {max_nombre_m} - Altura: {max_altura} cm")
        else:
            print(f"\n----------------- \nEl nombre del Superheroe Masculino mas alto es: {max_nombre_m}.")
    else:
        print("No se encontraron superheroes masculinos")

    return max_nombre_m

def max_altura_femenino(imprimir_altura=True):
    max_altura = None
    max_nombre_f = None

    chekpoint_max_altura = False
    
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            altura = round(float(personaje["altura"]))
            if max_altura is None or altura > max_altura:
                max_altura = altura
                max_nombre_f = personaje["nombre"]
                chekpoint_max_altura = True

    if chekpoint_max_altura:
        if imprimir_altura:
            print(f"\n----------------- \nSuperheroe mas alto: {max_nombre_f} - Altura: {max_altura} cm")
        else:
            print(f"\n----------------- \nEl nombre del Superheroe Femenino mas alto es: {max_nombre_f}.")
    else:
        print("No se encontraron superheroes femeninos")

    return max_nombre_f

def min_altura_masculino(imprimir_altura=True):
    min_altura = None
    min_nombre_m = None

    chekpoint_max_altura = False
    
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            altura = round(float(personaje["altura"]))
            if min_altura is None or altura < min_altura:
                min_altura = altura
                min_nombre_m = personaje["nombre"]
                chekpoint_max_altura = True

    if chekpoint_max_altura:
        if imprimir_altura:
            print(f"\n----------------- \nSuperheroe mas alto: {min_nombre_m} - Altura: {min_altura} cm")
        else:
            print(f"\n----------------- \nEl nombre del Superheroe Masculino mas bajo es: {min_nombre_m}.")
    else:
        print("No se encontraron superheroes masculinos")

    return min_nombre_m

def min_altura_femenino(imprimir_altura=True):
    min_altura = None
    min_nombre_f = None

    chekpoint_max_altura = False
    
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            altura = round(float(personaje["altura"]))
            if min_altura is None or altura < min_altura:
                min_altura = altura
                min_nombre_f = personaje["nombre"]
                chekpoint_max_altura = True

    if chekpoint_max_altura:
        if imprimir_altura:
            print(f"\n----------------- \nSuperheroe mas alto: {min_nombre_f} - Altura: {min_altura} cm")
        else:
            print(f"\n----------------- \nEl nombre del Superheroe Femenino mas bajo es: {min_nombre_f}.")
    else:
        print("No se encontraron superheroes femeninos")

    return min_nombre_f

def promedio_altura_masculino():
    altura_total = 0
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            altura_total += float(personaje["altura"])
    promedio_masculino = round(altura_total) / len(lista_personajes)
    print(f"\n----------------- \nAltura promedio de los superhéroes Masculinos: {promedio_masculino} cm")

def promedio_altura_femenino():
    altura_total = 0
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            altura_total += float(personaje["altura"])
    promedio_femenino = round(altura_total) / len(lista_personajes)
    print(f"\n----------------- \nAltura promedio de los superhéroes Femeninos: {promedio_femenino} cm")

def nombre_max_altura_masculino():
    max_altura = None
    max_personaje = None
    chekpoint_max_altura = False
    print("Personaje Masculino mas alto:")
    
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            altura = round(float(personaje["altura"]))
            if max_altura is None or altura > max_altura:
                max_altura = altura
                max_personaje = personaje["nombre"]
                chekpoint_max_altura = True

    if chekpoint_max_altura:
        print(f"\n----------------- \nSuperheroe mas alto: {max_personaje} ")
    else:
        print("No se encontraron superheroes masculinos")

def informe_de_nombres():
    max_personaje_masculino = max_altura_masculino(imprimir_altura=False)
    max_personaje_femenino = max_altura_femenino(imprimir_altura=False)
    min_personaje_masculino = min_altura_masculino(imprimir_altura=False)
    min_personaje_femenino = min_altura_femenino(imprimir_altura=False)

def contar_heroes_ojos(lista_personajes):
    contador_colores = {}
    for personaje in lista_personajes:
        color_ojos = personaje["color_ojos"]
        if color_ojos not in contador_colores:
            contador_colores[color_ojos] = 1
        else:
            contador_colores[color_ojos] += 1

    for color, cantidad in contador_colores.items():
        print(f"\n----------------- {color}: {cantidad}")
    
    return contador_colores

def contar_heroes_pelo(lista_personajes):
    contador_pelo = {}
    for personaje in lista_personajes:
        color_pelo = personaje["color_pelo"]
        if color_pelo is "":
            color_pelo = "No tiene"
        if color_pelo not in contador_pelo:
            contador_pelo[color_pelo] = 1
        else:
            contador_pelo[color_pelo] += 1

    for color, cantidad in contador_pelo.items():
        print(f"\n----------------- {color}: {cantidad}")
    
    return contador_pelo

def contar_heroes_iq(lista_personajes):
    contador_iq = {}
    personajes_sin_iq = []
    
    for personaje in lista_personajes:
        iq = personaje["inteligencia"]
        if iq is "":
            personajes_sin_iq.append(personaje)
            iq = print(f"\n----------------- No tiene - {personaje['nombre']}")
        
        if iq not in contador_iq:
            contador_iq[iq] = 1
        else:
            contador_iq[iq] += 1

    for iq_cantidad, cantidad in contador_iq.items():
        print(f"\n----------------- {iq_cantidad}: {cantidad}")

    return contador_iq

def listar_heroes_por_ojos(lista_personajes):
    heroes_por_ojos = {}
    for personaje in lista_personajes:
        color_ojos = personaje["color_ojos"]
        if color_ojos not in heroes_por_ojos:
            heroes_por_ojos[color_ojos] = []
        heroes_por_ojos[color_ojos].append(personaje["nombre"])

    for color_ojos, heroes in heroes_por_ojos.items():
        print(f"\n Superhéroes con ojos de color {color_ojos}:")
        for heroe in heroes:
            print(f" \n- {heroe}")

def listar_heroes_por_pelo(lista_personajes):
    heroes_por_pelo = {}
    for personaje in lista_personajes:
        color_pelo = personaje["color_pelo"]
        if color_pelo not in heroes_por_pelo:
            heroes_por_pelo[color_pelo] = []
        heroes_por_pelo[color_pelo].append(personaje["nombre"])

    for color_pelo, heroes in heroes_por_pelo.items():
        print(f"\n Superhéroes con pelo de color {color_pelo}:")
        for heroe in heroes:
            print(f"\n- {heroe}")

def listar_heroes_por_iq(lista_personajes):
    heroes_por_iq = {}
    for personaje in lista_personajes:
        inteligencia_iq = personaje["inteligencia"]
        if inteligencia_iq not in heroes_por_iq:
            heroes_por_iq[inteligencia_iq] = []
        heroes_por_iq[inteligencia_iq].append(personaje["nombre"])

    for inteligencia_iq, heroes in heroes_por_iq.items():
        print(f"\n Superhéroes con inteligencia {inteligencia_iq}:")
        for heroe in heroes:
            print(f"\n- {heroe}")

#------------------------------------------------/FUNCIONES-#02/---------------------------------------------#

def normalizador_datos_stark(lista_personajes):
#---------------------------

    """
    DOCUMENTACION:: Función que recibe una lista de héroes y convierte al tipo de dato correcto solicitado en la consigna, 
    en este caso... serian las keys (solo con las keys que representan datos numéricos) y valida primero que el tipo de dato
    no sea del tipo al cual será casteado para evitar confusiones.

    PARAMETROS: lista_heroes (list): es la lista que va a tomar para normalizar los datos obtenidos y solicitados.

    RETORNO:  (list): Lista de héroes normalizada.
    """

#---------------------------

    if not lista_personajes: # Compruebo si la lista esta vacia con el if not, y si lo esta retorno el resultado del print.
        print("Error: Lista de héroes vacía")
        return lista_personajes
    
    dato_modificado = False # Compruebo que el dato fue modificado a travez de una bandera.
    
    for heroe in lista_personajes:
        for key, value in heroe.items():
            if key in ["altura", "peso", "fuerza"]:
                if isinstance(value, str) and value.replace('.', '', 1).isdigit():
                    if "." in value:
                        heroe[key] = float(value)
                    else:
                        heroe[key] = int(value)
                    dato_modificado = True
    
    if dato_modificado:
        print("Datos normalizados")
    
    return lista_personajes

def obtener_nombre(heroe):
    return f"Nombre: {heroe['nombre']}"

lista_personajes = [...] # lista de diccionarios con los personajes

if not lista_personajes:
    print("Error: Lista de personajes vacía")
else:
    for heroe in lista_personajes:
        print(obtener_nombre(heroe))