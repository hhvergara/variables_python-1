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

    # Imprimir la cantidad de letras que posee su nombre complet
    print ("La cantidad de letras de mi nombre es:", len(nombre_completo))

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()