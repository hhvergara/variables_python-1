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
    print ("El primer numero a operar es:", numero_1)
    print ("El segundo numero a operar es:", numero_2)
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
    print(" Por ultimo, al multiplicar ambos valors obtenemos:", multiplicacion)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
ej2()