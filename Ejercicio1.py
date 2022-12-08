"""
Realizar un programa que muestre la tabla de
multiplicar de uno numero, de la forma siguiente
(metéis los resultados dentro de un array y presentáis por pantalla):
"""
numero = 5
resultados = []
multiplicar = 0

for i in range(11):
    multiplicar = numero*i
    resultados=[multiplicar]
    for j in resultados:
        print(numero,"x",i,"=",j)

"""
#l=[0,10,20,30,40,50,60,70,80,90,100]
l = []
i = 0
r= 0
while i < 11:
    r = 10*i
    l.append(r)
    i+=1
"""
"""
l = [0,0,0,0,0,0,0,0,0,0,0]
i = 0
r= 0
while i < 11:
    r = 10*i
    l[i] = r
    i+=1
"""
"""
i=0
while i<len(l):
   print(i,"x 10 =",l[i])
   i+=1 
"""