"""
Haced un programa que lea 10 números en coma flotante,
y posteriormente calcule:
• la suma de todos ellos.
• nos diga la cantidad de números negativos.
• reemplace los números negativos por su valor absoluto ( valor sin signo)
• muestre la lista resultante anterior.
"""
numeros = [2.3,4.5,5.7,7.6,-6.7,3.1,-3.4,1.6,3.6,6.0]
suma = 0
negativos = []
cantidad = 0
numeros_absolutos = []
#sumar los valores de una lista
i = 0
suma=0
while i < len(numeros):
    suma =suma + numeros[i]
    i+=1
print("El resultado de la suma es:",suma)
#cantidad negativos contar
for numero in numeros:
    if numero < 0:
        negativos.append(numero)
cantidad = len(negativos)
print("La cantidad de negativos son:",cantidad)
#remplazar negativos valor absoluto en lista original (hacer copia)
numeros2 = numeros.copy()
for numero in numeros2:
    if numero < 0:
        absoluto = -1*(numero)
        numeros2.remove(numero)
        numeros2.append(absoluto)
print("La lista original: ",numeros)
#mostrar la lista sin negativos
print("La lista con los valores absolutos: ",numeros2)