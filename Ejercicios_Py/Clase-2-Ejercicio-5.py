# Quimey Alejo Fontan - Programacion - DIV B - Giovanni
# Ejercicio 05
# Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento
# de HR dispone de lista de justicieros pero solo tiene información detallada de algunos de
# ellos.
# Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista
# heroes_info se puedan listar los datos de cada héroe con el siguiente formato.
# TIP: Las habilidades están repetidas, buscá la manera de que en el resultado final no existan
# duplicados, que usarías para eso?

heroes_info = [
    {"Nombre": "Super Girl",
    "ID": 1,
    "Origen": "Krypton",
    "Habilidades": ["Volar", "Fuerza", "Velocidad","Volar","Fuerza", "Velocidad"],
    "Identidad": "Kara Zor-El"},

    {"Nombre": "Power Girl", 
    "ID": 14,
    "Origen": "Krypton",
    "Habilidades": ["Volar", "Fuerza", "Congelar","Congelar","Congelar",],
    "Identidad": "Kara Starr"
    },

    {"Nombre": "Shazam", 
    "ID": 25,
    "Origen": "Tierra",
    "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia"],
    "Identidad": "Billy Batson"
    },

    {"Nombre": "Wonder Woman", 
    "ID": 25,
    "Origen": "Amazonia",
    "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
    "Identidad": "Diana Prince"
    }
]

habilidades_unicas = set()

for heroe in heroes_info:
    print("Nombre: {}".format(heroe["Nombre"]))
    print("ID: {}".format(heroe["ID"]))
    print("Origen: {}".format(heroe["Origen"]))
    habilidades = list(set(heroe["Habilidades"]))
    print("Habilidades: {}".format(", ".join(heroe["Habilidades"])))
    print("Identidad: {}".format(heroe["Identidad"]))
    print("-------------")
    
    habilidades_unicas.update(heroe["Habilidades"])

print("Habilidades únicas: {}".format(", ".join(sorted(habilidades_unicas))))
