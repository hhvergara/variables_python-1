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




if __name__ == '__main__':
    print("Ejercicios de práctica")
    
    ej2()