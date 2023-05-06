# mi_archivo = open("nombre_archivo1.txt", "a", encoding="utf-8")

# mi_archivo.write("Rampi")

# mi_archivo.close()

# mi_archivo = open("nombre_archivo1.txt", "a", encoding="utf-8")

# registro = mi_archivo.write("Rampi\n")

# mi_archivo.close()

# print(registro)

# lista = ["Fernando Fulbo","Luis LoL","Valentina Valle del Stardy no se cuanto"]

# with open("lista_nombres.txt", "w") as mi_archivo:
#     for nombres in lista:
#         mi_archivo.write(f"{nombres}\n")


# mi_archivo = open("lista_nombres.txt", "r")
# lista = mi_archivo.read()
# for line in lista:
#     print(lista, end="")

# mi_archivo = open("lista_nombres.txt", "r") as mi_archivo
# for line in mi_archivo:
#     print(mi_archivo, end="")

##CSV

# nombres = ["Gregorio", "Lara", "Matias"]
# apellidos = ["Andrade", "De La Cerda", "Cossu"]
# edades =  ["22", "26", "22"]
# TAM = 3

# with open("nombres.csv", "w") as mi_archivo:
#     for i in range(TAM):
#         registro = "{0},{1},{2}\n".format(nombres[i],apellidos[i],edades[i])
#         mi_archivo.write(registro)

# import re
# with open("agenda.csv", "r") as mi_archivo:
#     for line in mi_archivo:
#         registro = re.split(r"|\n,line")
#         print(f"{registro[0] - registro[1] - registro[2]}")

import json

# data = {}
# data ["Alumnos"] = []
# data ["Alumnos"].append({"nombre": "Juan", "edad": "20"})
# data ["Alumnos"].append({"nombre": "Maria", "edad": "22"})
# data ["Alumnos"].append({"nombre": "Puan", "edad": "23"})

# with open("data.json", "w") as mi_archivo:
#     json.dump(data, mi_archivo, indent=4)

with open("data.json", "r") as mi_archivo:
    data = json.load(mi_archivo)

print(data)