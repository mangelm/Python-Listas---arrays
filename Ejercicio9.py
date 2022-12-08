"""
El objetivo del programa es multiplicar por 2 el número que hemos leído
y mostrar el resultado (en binario).
Recordáis que multiplicar por 2 en binario es desplazar la cifra a la izquierda
, poniendo un cero al bit menos significativo. Miráis el ejemplo de la figura:
El bit descartado se avisa que se ha perdido.

"""

b = [1,0,1,0,1,0,0,1]
i = len(b)-1
aux = 0
ant = 0

while i >= 0:
   aux = b[i]
   b[i] = ant
   ant = aux
   i-=1

if ant == 1:
    print("overflow")
print(b)