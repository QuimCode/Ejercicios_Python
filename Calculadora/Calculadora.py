def sumar_numeros(numero_1:int, numero_2:int)->int: 

    suma = numero_1 + numero_2
    return suma

def restar_numeros(numero_1:int, numero_2:int)->int:

    resta = numero_1 - numero_2
    return resta

def multiplicar_numeros(numero_1:int, numero_2:int)->int:

    multiplicacion = numero_1 * numero_2
    print(f"El resultado de la multiplicacion es... {multiplicacion} ")
    return multiplicacion

def dividir_numeros(numero_1:int, numero_2:int)->float:
    
    division = None
    if numero_2 != 0:
        division = numero_1 / numero_2
    return division

chekpoint_ingreso = False

while True:
    opcion = int(input("\n¿Qué dato desea obtener? \n1. Ingresar Numero \n2. Restar \n3. Sumar \n4. Multiplicar \n5. Dividir \n6. Salir"))

    match opcion:
        case 1:
            y = int(input("Ingrese un numero"))
            x = int(input("Ingrese un numero"))
            chekpoint_ingreso = True
        case 2:
            if chekpoint_ingreso == True:
                resultado = restar_numeros(x, y)
                print(f"El resultado de la resta es... {resultado} ")
            else:
                print("No hay operadores ingresados.")
        case 3:
            if chekpoint_ingreso == True:
                resultado = sumar_numeros(x, y)
                print(f"El resultado de la suma es... {resultado} ")
            else:
                print("No hay operadores ingresados.")
        case 4:
            if chekpoint_ingreso == True:
                resultado = multiplicar_numeros(x, y)
                print(f"El resultado de la division es... {resultado} ")
            else:
                print("No hay operadores ingresados.")
        case 5:
            if chekpoint_ingreso == True:
                resultado = dividir_numeros(x, y)
                if(resultado != None):
                    print(f"El resultado de la resta es... {resultado} ")
                else:
                    print("No se puede dividir por 0")
            else:
                print("No hay operadores ingresados.")
        case 6:
            break
