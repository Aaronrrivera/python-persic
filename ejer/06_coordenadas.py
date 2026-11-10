#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. 
#Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. 
#En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa mostrando la lista 
#de coordenadas

#segunda version, pedir al usuario coordenadas y mostrar su posicion mas cercana a una de las tiendas
import math
import csv
coordenadas=[]
distancias=[]

cont=0

with open("coordenadas.csv","r") as f:
    lector=csv.reader(f)
    for fila in lector:
        x=int(fila[0])
        y=int(fila[1])
        coordenadas.append((x,y))

def distancia(p1,p2):
    distancia=math.hypot(p1[0]-p2[0],p1[1]-p2[1])
    return distancia

pos_usuario=(int(input("tu posicion x: ")), int(input("tu posicion Y: ")))
dir_fichero="coordenadas.csv"
distancia_corta=None
coordenada_tienda=None
with open(dir_fichero,"r") as f:
    coordenadas=csv.DictReader(f)
    for row in coordenadas:
        if distancia_corta==None:
            distancia_corta=distancia(row["x"],row["y"],pos_usuario)
        if coordenada_tienda==None:
            coordenada_tienda=(row["x"],row["y"])
    dist=distancia((row["x"],row["y"],pos_usuario))
    if dist<distancia_corta:
        distancia_corta,coordenada_tienda=dist,(row,["x"],row["y"])
print(f"la tienda mas cercana a {pos_usuario} tiene coordenadas en {coordenada_tienda}")