#Cargamos de una lista de diccionarios cada dicionario tiene que tener 3 claves nombre artista genero

def cargar_canciones(archivo):
    list=[]
    with open(archivo,"r") as fichero:
        for linea in fichero:
            cancion={}
            nombre, artista, genero=linea.strip().split(" - ")
            cancion["nombre"]=nombre
            cancion["artista"]=artista
            cancion["genero"]=genero
            list.append(cancion)
    return list


def añadir_canciones(list,nombre,artista,genero):
    #comprobar que esta
    for cancion in list:
        print(cancion.values())

playlist=cargar_canciones("playlist.txt")
añadir_canciones(playlist,"1 Enero","JC Reyes","trap")