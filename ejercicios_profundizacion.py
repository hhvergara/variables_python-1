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
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7
    '''
    print('Ingrese el primer número a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número a operar:')
    numero_2 = int(input())

    def operacion():
      suma = numero_1 + numero_2
      resta = numero_1 - numero_2
      Multiplicacion = numero_2 * numero_2
      division = numero_1 / numero_2
      potencia = numero_1 ** numero_2

      print("El resultado de la suma entre", numero_1, "y", numero_2, "es:", suma)
      print("El resultado de la resta entre", numero_1, "y", numero_2, "es:", resta)
      print("El resultado de la multilicacion entre", numero_1, "y", numero_2, "es:", Multiplicacion)
      print("El resultado de la division entre", numero_1, "y", numero_2, "es:", division)
      print("El resultado de la potencia entre", numero_1, "y", numero_2, "es:", potencia)

    operacion()
  


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
    
    print('Indique su Nombre Completo:')
    nombre_completo = str(input())
    
    print('por favor, ingrese su DNI:')
    dni = int(input())

    print('Ahora, indique su edad:')
    edad = int(input())

    print('por ultimo, indique su altura:')
    altura = float(input())

    print("\n")

    print("Confirme que los datos ingresados sean los correctos:\n\nSu nombre es",
    nombre_completo,", esta inscripto con el DNI Nro.:",dni, ", tiene", edad, 
    "años de edad y su altura de es de:", str(altura),"cm.")



def ej3():
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
    print('Ejercicios de práctica con cadenas')
    print("_______________O______________________\n")



    print("Puede indicar el nombre completo de su padre?\n") 
    # Inovetip: La función print tiene seteado por defecto para que utilice \n no hace falta agregarlo.
    nombre_pa = str (input())

    print("y puede indicar el nombre de su madre?\n")
    nombre_ma = str (input())

    print("Gracias, ahora indiquenos su nombre:\n")
    mi_nombre = str (input())

    print("", "1. Nombre del Padre:"" "+ nombre_pa + "\n 2. Nombre de la madre:"" "+ nombre_ma + "\n 3. Su nombre es:"" " + mi_nombre )
    print("________________________O_______________________\n")

    nomb, segnom, ape1,ape2 = nombre_pa.split()
    
    print ("Ape pa:",ape1,ape2)

    nombma, segnombma, ape1ma = nombre_ma.split()
    
    print ("Ape ma:", ape1ma)
    print("______________O____________\n")

    mi_nomb_completo = (mi_nombre +str(" ") + ape1 + str(" ") + ape2 + str(", ") + ape1ma)
    # En estos casos también lo podes hacer así:
    # f'{mi_nombre} {ape1} {ape2}, {ape1ma}'
    # Queda mas corto y se lee mejor.
    
    print("Mi nombre completo es:", mi_nomb_completo)


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


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    # ej4()
    # ej5()
