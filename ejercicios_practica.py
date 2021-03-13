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

    # Imprimir en pantalla el resultado de la suma
    # print(....)

    # Repita el procedimiento para realizar la resta

    # realizamos la suma
    suma = numero_1 + numero_2

    # Imprimimos resultado
    print ('El resultado de la suma es:' , suma)

    # realizamos la resta
    resta = numero_1 - numero_2

    # Imprimimos el resulado
    print ('El resultado de la resta es:', resta)


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

    # Imprimo en pantalla los numeros ingresados
    print('El primer numero ingresado es:', numero_1)
    
    print('El segundo numero ingresado es:', numero_2)

    # Suma
    suma = numero_1 + numero_2
    
    # Resta
    resta = numero_1 - numero_2
    
    # Division
    division = numero_1 / numero_2
    
    # Multiplicacion
    multiplicacion = numero_1 * numero_2

    # Impresion de resultados
    print ('El resultado de sumar', numero_1, 'y', numero_2, 'es:', suma)
    
    print ('El resultado de restar', numero_1, 'y', numero_2, 'es:', resta)
    
    print ('El resultado de dividir', numero_1, 'y', numero_2, 'es:', division)
    
    print ('El resultado de multiplicar', numero_1, 'y', numero_2, 'es:', multiplicacion)



def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    nombre_completo = nombre +' '+ apellido
    print ('Su nombre completo es:', nombre_completo)

    # Cantidad de caracteres
    nombre_completolen = len(nombre_completo)
    print('Su nombre completo tiene:',nombre_completolen,'caracteres')




    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo


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
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

    letra_1 = palabra_1[0]
    letra_2 = palabra_2[0]
    letra_3 = palabra_3[0]

    print('El acronimo de sus palabras es:', letra_1, letra_2, letra_3)


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

    primeras_3 = palabra_1[:3]
    ultimas_3 = palabra_2[-3:]
    nueva_palabra = primeras_3 + ultimas_3
    print('La nueva palabra es:', nueva_palabra)



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
    
