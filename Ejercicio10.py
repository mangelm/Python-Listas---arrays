"""
Haced un programa que pida una lista de notas ( hasta que el usuario entre una nota negativa ), Una vez entradas:
mostrará las notas en orden inverso al de entrada.
mostrará la nota media
mostrará la varianza, que se calcula con la siguiente fórmula

x = media de todos los números
xi = y-èssim número de la lista
n = medida de la lista
finalmente el programa mostrará la desviación típica

Usáis la función sqrt(*num) de la librería math, hacer un “importe math” al inicio del código.
Ejemplo definido paso a paso de una forma sencilla: 2, 3, 6, 8, 11. (Se puede hacer como sale a la fórmula) N = 5 elementos

Media = (2+3+6+8+11)/5 = 6
varianza= (22+3*3+6*6+8*8+11*11)/5 – mediamedia
Desviación típica = Raíz cuadrada(varianza)

[8,2,5,5,4,6,9,1], resultado esperado 10,
valores continuos 8+2 =10, 2+5 no, 5+5 = 10, 5+4 no,4+6=10,6+9 no, 9+1 = 10
"""
import math

l = [1,4,3,5,6,1,5,7]
i = 0
m = 0
while i < len(l):
    m+= l[i]
    i+=1
m = m/len(l)
print("media",m)

i = len(l)-1
while i >= 0:
    print(l[i], ", ",end="")
    i-=1

i = 0
v = 0
while i < len(l):
    v+= l[i]**2 #l[i]*l[i]
    i+=1
v = v/len(l) - m**2
print("variancia",v)

dv = 0
dv = math.sqrt(v)
print("desviacio tipica", dv)

