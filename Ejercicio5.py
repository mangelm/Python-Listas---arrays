"""
Un programa para hacer votaciones nos permitirá
entrar por teclado y guardar en un array 6 votos.
El programa forzará que cada voto sea una
cifra del 0 al 10.
"""
vots = []
v = 0
i = 0
v = -1
while (i<6): 
    v = int (input())   
    if (v<0 or v>10):
        print ("Introdueixi vot vàlid")       
    else:
        vots.append(v)
        i+=1
print (vots)