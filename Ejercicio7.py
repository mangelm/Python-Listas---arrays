"""
Siguiendo con el programa de votaciones,
ahora queremos que el sistema descarte la
puntuación más alta y la más baja.
Muestra la lista sin el mes alto y
el mes bajo
"""
vots = [0,3,4,1,2,7,10,5,0,4,5,6,1]

pvmin = 0
pvmax = 0
i = 0
vmin = 0 #11
vmax = 0 #-1
vmin = vots[0]
vmax = vots[0]

while i < len(vots):
    if vmin >= vots[i]:
        vmin = vots[i]
        pvmin = i
    if vmax <= vots[i]:
        vmax = vots[i]
        pvmax = i 
    i+=1

#print("el voto max está en la pos", pvmax, " valor", vmax )
#print("el voto min está en la pos", pvmin, " valor", vmin )

avots = []

i=0
while i < len(vots):
    if vots[i] != vmax and vots[i]!= vmin:
        avots.append(vots[i])
    i+=1
print(avots)

media=0.0
i=0
while i < len(avots):
    media += avots[i]
    i+=1
media= media/len(avots)
print("la media sin los maximos y minimos es", media)