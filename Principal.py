#Cargamos de una lista de diccionarios cada dicionario tiene que tener 3 claves nombre artista genero
import json

#CARGAR CANCIONES DESDE TXT
def cargar_canciones(archivo):
    list=[]
    try:
        with open(archivo,"r") as fichero:
            for linea in fichero:
                cancion={}
                valores=linea.strip().split("  -  ")
                if (len(valores) ==3):
                    nombre, artista, genero = valores
                    cancion["nombre"]=nombre
                    cancion["artista"]=artista
                    cancion["genero"]=genero
                    list.append(cancion)
                else:
                    print("El formato tiene un numero de elementos erroneos\nTiene que tener 3 valores")
    except FileNotFoundError:
        print("archivo no encontrado")
    return list

#CARGAR CANCION DESDE JSON

#AÑADIR CANCION
def añadir_canciones(nombre,artista,genero):
    #comprobar que esta
    esta=False
    for cancion in playlist:
        if cancion["nombre"]!=nombre or cancion["artista"]!=artista:
            esta=True
        
    if esta==True:
        nuevaCancion={}
        nuevaCancion["nombre"]=nombre
        nuevaCancion["artista"]=artista
        nuevaCancion["genero"]=genero
        playlist.append(nuevaCancion)
        print("La cancion se ha añadido")
    else:
        print("La cancion ya está añadida")

#BUSCAR CANCION
def buscar_cancion(nombre):
    for cancion in playlist:
        if cancion["nombre"]==nombre:
            return(cancion)
    return ("No se ha encontrado la canción")

#ELIMINAR UNA CANCION
def eliminar_canciones(nombre,artista):
    eliminado=False
    for cancion in playlist:
        if cancion["nombre"]==nombre:
            playlist.remove(cancion)
            eliminado=True
    
    if eliminado==True:
        print("Se ha eliminado la canción")
    else:
        print("No está la canción")

#GUARDAR DATOS TXT
def guardar_datos(archivo):
    try:
        with open(archivo, "w") as fichero:
            for cancion in playlist:
                fichero.write(cancion["nombre"]+"  -  "+cancion["artista"]+"  -  "+cancion["genero"]+"\n")
    except FileNotFoundError:
        print("archivo no encontrado")

#GUARDAR DATOS EN JSON
playlist=cargar_canciones("playlist.txt")
añadir_canciones("1 Enero","JC Reyes","trap")
print(buscar_cancion("1 Enero"))
eliminar_canciones("1 Enero","JC Reyes")
guardar_datos("playlist.txt")
print(playlist)