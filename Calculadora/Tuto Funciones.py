    #------------FUNCIONES A EVITAR NO RETORNAR NI TIENE PARAMETROS----------------------------------------------------------------------------#


def sumar_numeros(): #Aca se implementan/definen las funciones 
    
    '''
    Brief: Funcion de suma...
    Parameter:
    Retorno: Esta funcionretornaria la suma de dos numeros.
    '''

    numero_1 = int(input("Ingrese el primer numero"))
    numero_2 = int(input("Ingrese el segundo numero"))

    suma = numero_1 + numero_2

    print(f"La suma es: {suma}") # "f" Interpolar = buscar 

    #------------FUNCIONES QUE SE SALVAN SOLO RETORNO--------------------------------------------------------------------------#

def restar_numeros():#Aca retorna la informacion con #return, estaria 
# retornando un int 

    numero_1 = int(input("Ingrese el primer numero"))
    numero_2 = int(input("Ingrese el segundo numero"))

    resta = numero_1 - numero_2

    return resta # El return lo que hace es establecer y devolver un paremetro de
# la funcion a una variable establecida, en este caso "resta", asignandole ese valor 
# luego cuando se llame la funcion 

    #------------FUNCIONES QUE SE SALVAN SOLO PARAMETROS-----------------------------------------------------------------#


def multiplicar_numeros(numero_1:int, numero_2:int): # Se explicitan los numeros
# formales con su composicion ya sea int o float, son formales por que nunca cambian
# y se establezcan mas delante cuando se llame la funcion.

    multiplicacion = numero_1 * numero_2
    print(f"El resultado de la multiplicacion es... {multiplicacion} ")

    #-------------FUNCIONES QUE SI SE DEBEN USAR RETORNO/PARAMETROS-----------------------------------------------------------------#
    # Los parametros pueden ser un poco discutible si usar o no, aunque si se usan
    # Mientras que el retorno si es necesario para verificar si la funcion lo logro o no

def dividir_numeros(numero_1:int, numero_2:int)->float:
    
    division = None
    if numero_2 != 0:
        division = numero_1 / numero_2

    return division

def potenciar(base, exponente):
    return base**exponente

    #----------------------------------------------------------------------------------------------------#

print("Hola... Bienvenidos a mi programa...") 
sumar_numeros() #Asi se llama a la funcion para ejecutarse
print("Grcias por su suma....")

resta_numero = restar_numeros()
print(f"El resultado de la resta es... {resta_numero}")

multiplicar_numeros(5,9) #Aplicar numeros que se pide en la funcion 
# "Numeros actuales" ya que son el sinonimo de lo que se pide en los formales, pero
# aca cambian dependiendo lo que uno desee multiplicar, teniendo en cuenta el "int"
# o "float" de los formales establecidos arriba en la funcion.

resultado_division = dividir_numeros(6,2) # Se aplican "Numeros Actuales" de nuevo
if(resultado_division != None):
    print(f"El resultado de la division es... {resultado_division}")
else:
    print("El divisor es 0")

base = 2
exponente = 3

resultado = potenciar(base, exponente)

print(resultado)

