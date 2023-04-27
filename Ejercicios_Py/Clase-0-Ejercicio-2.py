#Quimey Alejo Fontan - Programacion - DIV B - Giovanni

reglas = {
    1: "Utilizar 4 espacios para la identacion",
    2: "Las lineas no deben superar los 79 caracteres",
    3: "Utilice lineas en blanco para separar funciones y clases",
    4: "Use espacios alrededor de los operadores y después de las comas",
    5: "Use comillas simples o dobles de manera consistente",
    6: "Siga las convenciones de nombrado de Python (lowercase_with_underscores para variables y funciones)",
    7: "Coloque los imports en líneas separadas al principio del archivo",
    8: "No use espacios en blanco al final de las líneas",
}

numero = int(input("Ingrese un numero entre 1 y 8"))
if numero in reglas:
    print("Regla {numero}: {reglas}[numero]}")
else:
    print("Error, regla de estilo inexistente”")