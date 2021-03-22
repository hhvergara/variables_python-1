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

    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....
    operacion_suma = numero_1 + numero_2
    print('El resultado de la suma de', numero_1, 'y', numero_2, 'es', operacion_suma)
    

    # Imprimir en pantalla el resultado de la suma
    # print(....)

    # Repita el procedimiento para realizar la resta
    operacion_resta = numero_1 - numero_2
    print('El resultado de la resta de', numero_1, 'y', numero_2, 'es', operacion_resta)


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
    print('El numero elegido es', numero_2)
    suma = numero_1 + numero_2
    print('el resultado de la suma de', numero_1, 'y', numero_2, 'es',suma)
    # Resta
    resta = numero_1 - numero_2
    print('el resultado de la resta de', numero_1, 'y', numero_2, 'es', resta)
    # División
    division = numero_1 / numero_2
    print('el resultado de la division de', numero_1, 'y', numero_2, 'es', division)
    # Multiplicación
    multiplicacion = numero_1 * numero_2
    print('el resultado de la multiplicacion de', numero_1, 'y', numero_2, 'es', multiplicacion)
  


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo

    nombre_completo = nombre.capitalize() + ' ' + apellido.capitalize()
    print(nombre_completo)
    letras = len(nombre_completo)
    print(nombre_completo, 'posee', letras-1, 'letras')


def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra1 = str(input())

    print('Ingrese palabra 2:')
    palabra2 = str(input())

    print('Ingrese palabra 3:')
    palabra3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

    print('Ingrese palabra 4:')
    palabra4 = str(input())
    # coloque concatenador + para que en la sigla salgan los acronimos juntos, 
    # porque con coma(,) separa la sigla a armar con un espacio
    print('La union de acronimos forma la sigla', palabra1[0].capitalize()
    +palabra2[0].capitalize()+palabra3[0].capitalize()+palabra4[0].capitalize())


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados
    # Inovetip: en la línea de abajo, le falta un espacio en el indentado :D
   NuevaPalabra= palabra_1[0:3]+palabra_2[2:6] # En esta línea, fijate que podes hacer palabra_1[0:3]+palabra_2[-3:] para que funcione
    # para cualquier palabra :D
    print(NuevaPalabra)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
