#Cargamos de una lista de diccionarios cada dicionario tiene que tener 3 claves nombre artista genero

def cargar_canciones(archivo):
    list=[]
    with open(archivo,"r") as fichero:
        for linea in fichero:
            cancion={}
            nombre, artista, genero=linea.strip().split("  -  ")
            cancion["nombre"]=nombre
            cancion["artista"]=artista
            cancion["genero"]=genero
            list.append(cancion)
    return list


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

def guardar_datos(archivo):
    with open(archivo, "w") as fichero:
        for cancion in playlist:
            fichero.write(cancion["nombre"]+"  -  "+cancion["artista"]+"  -  "+cancion["genero"]+"\n")

playlist=cargar_canciones("playlist.txt")
añadir_canciones("1 Enero","JC Reyes","trap")
eliminar_canciones("1 Enero","JC Reyes")
guardar_datos("playlist.txt")
print(playlist)