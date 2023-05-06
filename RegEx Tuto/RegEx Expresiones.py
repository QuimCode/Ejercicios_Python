import re

# #SPLIT

# print(re.split(" ", "hola mundo"))

# print(re.split("[a-z ]", "hola mundo 125c")) #[a-z ] de esta forma quita y busca de la A a la Z caracter por caracter y te los imprime

# print(re.split("[a-z ]+", "hola mundo 125c")) #[a-z ]+ de esta forma quita y busca de la A a la Z caracter por caracter, pero te lo imprime una sola vez asi (" ") los muestra en un conjunto

# print(re.split("[a-z]|[0-9]", "hola mundo 125 chau")) #[a-z]|[0-9] de esta forma quita y busca de la A a la Z OR/O/| del 0 al 9 caracter por caracter, imprimiendo los que encontro eliminandolos

# #SEARCH

# print(re.search("como", "hola mundo ¿ como estan ?").span())

# print(re.search("como", "hola mundo ¿ como estan ?").start())

# print(re.search("como", "hola mundo ¿ como estan ?").end())

# print(re.search("[0-9]+", "texto con numeros: 123455643 y letras: aaaaaaa"))#Cadena con numeros y letras que busca un patron de 1 o mas ocurrencias (una pegadita al lado de la otra) pero esta con "+" que eso lo que hace es bucar un numero pegadito del otro, mientras que si lo saco, busca caracter por caracter.

# print(re.search("[0-9]+", "texto con numeros: 123455643 y letras: aaaaaaa").group())

#FINDALL

# texto = "uno 1 dos 2 y tres 3 mas el cuarenta y cuatro 44"

# print(re.findall(" ", texto))

# print(re.findall("[0-9]+", texto))# El 44 lo muestra junto ya que esta el + y eso muestra en formato de conjunto los numeros o caracteres que esten pegados, si sacara el + me los mostraria uno por uno

# print(re.findall("[a-z]+", texto))

# print(re.findall("[a-zA-Z]+", texto))# Esto incluye las mayusculas si por ejemplo seria Uno, Dos, Tres

# print(re.findall("[a-zA-Z]{3}", texto))#Esto me trairia un conjunto de solo LOS 3 PRIMEROS CARACTERES que se ven, AUNQUE tambien puede ser {3,6} para incluir las palabras con 3 y 6, ya que si se deja 3 solamente mostraria "Uno", "Dos", "Tre"

#SUB 

texto = "abc abc cccc abc ddd aaa    abc ddd abd abc"

result = re.sub("abc ", " ", texto)#Sirve para suplantes, primero se pone que cosa voy a buscar "abc", por que cosa voy a suplantar " ", y el lugar donde lo voy a buscar "texto" (variable)
print(result)

result = re.sub(r"\s+", " ", texto)

print(texto)
print(result)