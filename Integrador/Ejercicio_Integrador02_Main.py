#----------------------------------------------------------------------------------------------------#

# Quimey Alejo Fontan - Programacion - DIV B - Giovanni - MENU-01
# Desafío #02: (con biblioteca propia: stark_biblioteca)
# En base a lo resuelto en el desafío #00, deberás mejorar la calidad de tus funciones.
# Es por ello que te proponemos lo siguiente:
# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
# escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
# un string, etc y que contendrá) y que es lo que retorna la función!

#------------------------------------------------/EXPORTACIONES/----------------------------------------#

from data_stark import lista_personajes 
from Funciones import *

#---------------------------------------------------/MENU/--------------------------------------------#

while True:
    opcion = int(input("\n¿Qué dato desea obtener? \n"
                            "1. Convertidor de Datos \n"
                            "2. Nombre de Heroes \n"
                            "3. Altura Maxima Masculino \n"
                            "4. Altura Maxima Femenino \n"
                            "5. Altura Minima Masculino \n"
                            "6. Altura Minima Femenino \n"
                            "7. Promedio de Altura Masculino \n"
                            "8. Promedio de Altura Femenino \n"
                            "9. Nombre de la Altura Maxima Masculina \n"
                            "10. Nombres de las Alturas \n"
                            "11. Tipo de Ojos \n"
                            "12. Tipo de Pelo \n"
                            "13. Tipo de IQ \n"
                            "14. Lista Heroes Ojos \n"
                            "15. Lista Heroes Pelo \n"
                            "16. Lista Heroes IQ \n"
                            "17. Salir \n"
                            "Ingrese un numero por favor: "))

    match opcion:
            case 1:
                normalizador_datos_stark(lista_personajes)
            case 2:
                stark_imprimir_nombres_heroes(lista_personajes)
            case 3:
                stark_imprimir_nombres_alturas(lista_personajes)
            case 4:
                max_altura_femenino()
            case 5:
                min_altura_masculino()
            case 6:
                min_altura_masculino()
            case 7:
                promedio_altura_masculino()
            case 8:
                promedio_altura_femenino()
            case 9:
                nombre_max_altura_masculino()
            case 10:
                informe_de_nombres()
            case 11:
                contar_heroes_ojos(lista_personajes)
            case 12:
                contar_heroes_pelo(lista_personajes)
            case 13:
                contar_heroes_iq(lista_personajes)
            case 14:
                listar_heroes_por_ojos(lista_personajes)
            case 15:
                listar_heroes_por_pelo(lista_personajes)
            case 16:
                listar_heroes_por_iq(lista_personajes)
            case 17:
                break