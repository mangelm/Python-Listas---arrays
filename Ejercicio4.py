"""
Haced un programa que imprima por pantalla
de forma consecutiva la serie de caracteres siguiente:
- , \ , | , /
Después de imprimir cada carácter, el programa
leerá una letra del teclado. Si no es ‘F’, el
programa continúa, borra la pantalla y peine
el siguiente carácter de la lista, y vuelve a leer
una letra....y así sucesivamente.
Cuando se llega al último carácter se empieza por el primero.
Usáis un array para almacenar la lista de caracteres !
"""
import os

salida = input("Si quieres iniciar o continuar el ciclo, pulsa el botón Intro. Si quieres salir, pulsa el botón F.")
i = 0
caracteres = ['-','\\','|','/']
while salida != "f" and salida!= "F":
    os.system("cls")
    print(caracteres[i])
    i+=1

    if i == 4:
        i = 0
    salida = input("Si quieres iniciar o continuar el ciclo, pulsa el botón Intro. Si quieres salir, pulsa el botón F.")
"""
import os
sl=["-","\\","|","/"]
c=''
i=0
c=input()
while (c!='f'):
    os.system("cls")
    print (sl[i])
    i+=1
    if i == 4:
        i = 0
    c=input()

"""