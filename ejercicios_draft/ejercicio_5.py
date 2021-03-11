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
    
    # Formar una nueva palabra con los recortes solicitados
    palabra_nueva= palabra_1[0] + palabra_1[1] + palabra_1[2]+ palabra_2[3:]
    
    #Imprima en pantalla los resultados
    print(palabra_nueva)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej5()