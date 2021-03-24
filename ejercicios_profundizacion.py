#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    # Realizamos la operacion suma
    print('Ingrese el primer numero a sumar:')
    primer_numero = int(input())

    print('Ingrese segundo numero a sumar:')
    segundo_numero = int(input())

    suma = primer_numero + segundo_numero

    print('La suma entre el numero', primer_numero,
          'y', segundo_numero, 'es:', suma)

  	# Realizamos la operacion resta

    print('Ingrese el primer numero a restar:')
    primer_numero = int(input())

    print('Ingrese segundo numero a restar:')
    segundo_numero = int(input())

    resta = primer_numero - segundo_numero

    print ('La resta entre el numero', primer_numero, 'y', segundo_numero, 'es:', resta)
    
    # Realizamos la operacion multiplicacion
    print('Ingrese el primer numero a multiplicar:')
    primer_numero = int(input())

    print('Ingrese segundo numero a multiplicar:')
    segundo_numero = int(input())

    multiplicacion = primer_numero * segundo_numero

    print ('La multiplicacion entre el numero', primer_numero, 'y', segundo_numero, 'es:', multiplicacion)
    
    # Realizamos la operacion division

    print('Ingrese el primer numero a dividir:')
    primer_numero = int(input())

    print('Ingrese segundo numero o divisor:')
    segundo_numero = int(input())

    division = primer_numero / segundo_numero

    print ('La division entre el numero', primer_numero, 'y', segundo_numero, 'es:', division)

   # Realizamos la operacion potenciacion

    print('Ingrese el primer numero a exponenciar:')
    primer_numero = int(input())

    print('Ingrese segundo numero o exponente:')
    segundo_numero = int(input())

    potenciacion = primer_numero ** segundo_numero

    print ('La potenciacion entre el numero', primer_numero, 'elevado a la', segundo_numero, 'es:', potenciacion)


def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''
    # Solicitamos los datos de la persona en los formatos establecidos
    print('Ingrese su nombre :')
    nombre = str(input())
    print('Ingrese su apellido:')
    apellido = str(input())
    nombre_completo = nombre + ' ' + apellido
    print('Ingrese su numero de DNI:')
    numero_dni = int(input())
    print('Ingrese su edad:')
    edad = int(input())
    print('Ingrese su altura:')
    altura = float(input())

    # Mostramos en consola los datos solicitados

    print('Su nombre completo es:', nombre_completo, 'y su DNI es:', numero_dni)
    print('Su nombre completo es:', nombre_completo, 'su edad es', edad, 'años', 'y su altura es', altura,'cms')





def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''
    # Solicitamos ingrese nombre del primer padre y le asignamos el primer apellido
    print('Ingrese nombre y apellido de su padre')
    nombre_paterno = str(input())
    nombre_padre, apellido_padre = nombre_paterno.split(' ')

    # Solicitamos ingrese nombre del segundo padre y le asignamos el segundo apellido
    print('Ingrese el nombre y apellido de su madre')
    nombre_materno = str(input())
    nombre_madre, apellido_madre = nombre_materno.split(' ')
    
    # Solicitamos los nombres del hijo
    print('Ingrese su/s nombre/s:')
    nombre_hijo = str(input())
    # Mostramos en consola el resultado de los apellidos asignados
    print('Su nombre y apellidos completos son:', nombre_hijo,'', apellido_padre,'', apellido_madre)


def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    # Solicitamos se ingrese el nombre de las personas y definimos que tome unicamente el apellido de cada una
    print('Ingrese el nombre y apellido de la primer persona:')
    primer_persona = str(input())
    # Definimos que tome el apellido ingresado
    nombre_primera, apellido_primera = primer_persona.split(' ')

    print('Ingrese el nombre y apellido de la segunda persona')
    segunda_persona = str(input())

    # Establecemos sentencia condicional si esta contenido en apellido
    if apellido_primera in segunda_persona:
      print('Son parientes')
    # Establecemos sentencia condicional si no esta contenido
    else:
      print('No son parientes')


def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''

    # Solicitamos se ingrese nombre completo
    print('Ingrese su/s nombre/s y apellido/s completos:')
    nombre_completo = str(input())

    # Establecemos variable para minuscula
    nombre_minuscula = str.lower(nombre_completo)
    print('Su nombre completo en minusculas es:', nombre_minuscula)

    # Establecemos variable para mayusculas
    nombre_mayuscula = str.upper(nombre_completo)
    print('Su nombre completo en mayusculas es:', nombre_mayuscula)

    # Establecemos variable para primer letra en mayuscula
    nombre_1mayuscula = str.capitalize(nombre_completo)
    print('Su nombre completo con la primer letra es mayusculas es:', nombre_1mayuscula)


if __name__ == '__main__':
    print("Ejercicios de práctica")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()