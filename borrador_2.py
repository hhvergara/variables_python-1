def ej3():
    print('Ejercicios de práctica con cadenas')
    print("------------------------------------\n")

    
    print ("Puede indicar el nombre completo de su padre?\n")
    nombre_pa = str (input())

    print("y puede indicar el nombre de su madre?\n")
    nombre_ma = str (input())

    print("Gracias, ahora indiquenos su nombre\n")
    mi_nombre = str (input())

    print("", "Nombre del Padre:"" "+ nombre_pa + "\n Nombre de la madre:"" "+ nombre_ma + "\n Su nombre es:"" " + mi_nombre )

    nomb, segnom, ape1,ape2 = nombre_pa.split()
    
    print (ape1,ape2)

    nombma,segnombma, ape1ma = nombre_ma.split()
    
    print (ape1ma)

    mi_nomb_completo= (mi_nombre +str(" ")+ ape1 + str(" ") + ape2 + str(", ") + ape1ma)

    print("Mi nombre completo es:", mi_nomb_completo)


    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres
    
    

    ok Primero el programa debe consultar el nombre completo del padre_1
    ok Luego el programa debe consultar el nombre completo del padre_2
    ok Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle,' altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''
if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej3()
    


 


