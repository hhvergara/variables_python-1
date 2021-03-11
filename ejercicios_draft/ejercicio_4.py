# Palabra 1: Club Atletico Boca Juniors 
# Palabra 2: Objeto volador no identificado 
# Palabra 3: Gestion Integral Mandatarios



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
    
    
    club= palabra_1
    print("cantidad de letras=",len(club))
    print(palabra_1[0],".",palabra_1[5],".",palabra_1[14],".", palabra_1[19])

    objeto= palabra_2
    print("cantidad de letras=",len(objeto))
    print(palabra_2[0],palabra_2[7],palabra_2[15], palabra_2[18])
    
    soft= palabra_3
    print("cantidad de letras=",len(soft))
    print(palabra_3[0],palabra_3[8],palabra_3[17])
   

    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej4()    
