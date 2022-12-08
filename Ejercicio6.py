"""
Ampliáis el programa de votaciones anterior
para que indique cuál es la mejor
puntuación, la peor, y en qué posición
de la array se emitió cada una.
Por ejemplo, para la entrada { 1,2,4,3,6, 3 },
la salida seria:
*****************************************************
* Máxima puntuación: 6 puntos a la posición 4 *
* Mínima puntuación: 1 puntos a la posición 0 *
*****************************************************
"""
""" votos = [0,3,4,1,2,7,10,5,0,4,5,6,1]

posvotmin = 0
posvotmax = 0
i = 0
vmin = 0 #11
vmax = 0 #-1
vmin = votos[0]
vmax = votos[0]

while i < len(votos):
    if vmin >= votos[i]:
        vmin = votos[i]
        posvotmin = i
    if vmax <= votos[i]:
        vmax = votos[i]
        posvotmax = i 
    i+=1

print("el voto max está en la pos", posvotmax, " valor", vmax )
print("el voto min está en la pos", posvotmin, " valor", vmin ) """
vots = [0,3,4,1,2,7,10,5,0,4,5,6,1]

pvmin = 0
pvmax = 0
i = 0
vmin = 0 #11
vmax = 0 #-1

while i < len(vots):
    if vots[pvmin] >= vots[i]:
        pvmin = i
    if vots[pvmax] <= vots[i]:
        pvmax = i 
    i+=1

print("el voto max está en la pos", pvmax, " valor", vots[pvmax] )
print("el voto min está en la pos", pvmin, " valor", vots[pvmin] )  
