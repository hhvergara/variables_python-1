#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.5

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.5"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7
    
    operacion= numero_1 + numero_2
    print(operacion)
    
    print('######## LINEA ########')
    
    operacionresta = numero_1 - numero_2
    
    print(operacionresta)

    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....

    # Imprimir en pantalla el resultado de la suma
    # print(....)

    # Repita el procedimiento para realizar la resta


def ej2():
    # Ejercicios de práctica numérica

    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6
    # NOTA: No coloque usted los nùmeros y resultados, use las variables

    # Suma
    suma= numero_1 + numero_2
    print("El resultado de la sumatoria es:", suma)

    # Resta
    resta= numero_1 - numero_2
    print("Si restamos los campos nos arroja el valor de:", resta)

    # División
    division= numero_1 / numero_2
    print("En cambio, si dividios nos da:", division)

    # Multiplicación
    multiplicacion= numero_1 * numero_2
    print("Por ultimo, al multiplicar ambos valors obtenemos:", multiplicacion)


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    print(nombre, apellido)

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....
    nombre_completo= str(nombre +" " + apellido)
    print("Mi nombre completo es:", nombre_completo)

    # Imprimir la cantidad de letras que posee su nombre completo
    print ("La cantidad de letras de mi nombre es:", len(nombre_completo))


def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    print("","Palabra 1:", palabra_1,"\n","Palabra 2:", palabra_2,"\n","Palabra 3:", palabra_3)
    
    # De cada palabra debe tomar la primera letra y armar el acrónimo
    club= palabra_1
    print("cantidad de letras=",len(club))
    print(palabra_1[0],".",palabra_1[5],".",palabra_1[14],".", palabra_1[19])

    objeto= palabra_2
    print("cantidad de letras=",len(objeto))
    print(palabra_2[0],palabra_2[7],palabra_2[15], palabra_2[18])
    
    soft= palabra_3
    print("cantidad de letras=",len(soft))
    print(palabra_3[0],palabra_3[8],palabra_3[17])

    # Palabra 1: Club Atletico Boca Juniors 
    # Palabra 2: Objeto volador no identificado 
    # Palabra 3: Gestion Integral Mandatarios


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

     # De la primera palabra tome las primeras tres letras, utilice el operador :
    print(palabra_1[:3])
    
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    print(palabra_2[3:])
    # Inovetip: En esta línea tomas el rango desde el tercer caracter hacia adelante, 
    # tendrías que usar en realidad print(palabra_2[-3:]) para obtener las últimas tres, de esa manera te
    # independisas del tamaño de la palabra.
        
    # Formar una nueva palabra con los recortes solicitados
    palabra_nueva= palabra_1[0] + palabra_1[1] + palabra_1[2]+ palabra_2[3:]
    
    #Imprima en pantalla los resultados
    print(palabra_nueva)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
