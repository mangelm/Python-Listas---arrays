"""
Un profesor toma medidas de las alturas de sus
alumnos de su clase. Para cada uno de los 10
alumnos, toma las medidas dos veces en el año.
Haremos un programa que nos permita introducir 10
valores de altura (para la primera medida), y
10 valores para la segunda medida.
El programa nos mostrará un lista del crecimiento
experimentado para cada alumno.
"""
medidas1 = [1.70,1.80,1.50,1.95,1.60,1.70,1.86,1.93,1.67,1.87]
medidas2 = [1.71,1.82,1.53,1.95,1.64,1.73,1.87,1.95,1.69,1.89]
i = 0
res = 0

while (i < 10):
    res = medidas1[i] - medidas2[i]
    print ("La diferència d'alçada de l'alumne", i, "és de", res)
    i+=1

"""
medida1 = []
medida2 = []
diferencia=[]

altura = 0
altura1 = 0

i = 0

numlist = 0

while i <= 10:
    
    print("Primera medida de altura")
    altura = float(input())
    medida1.append(altura)

    print("Segunda medida de altura")
    altura1 = float(input())
    medida2.append(altura)

    diferencia.append(medida2[i] - medida1[i] )  

    i+=1

print("Lista: ",diferencia)
"""