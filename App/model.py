"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    
    catalog = {'artwork': None,
               'artists': None}

    catalog['artwork'] = lt.newList()
    catalog['artists'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareartists)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
 
    lt.addLast(catalog['artwork'], artwork)

    artists = artwork['artist'].split(",")
    for artist in artists:
        addArtwork(catalog, artist.strip(), artwork)  


def addArtist(catalog, artistname, artwork):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    artists = catalog['artists']
    posartist = lt.isPresent(artists, artistname)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newArtist(artistname)
        lt.addLast(artists, artist)
    lt.addLast(artist['artworks'], artwork)


# Funciones para creacion de datos
def newArtist(name):
    
    artist = {'DisplayName': "", "artworks": None}
    artist['DisplayName'] = name
    artist['artowrks'] = lt.newList('ARRAY_LIST')
    return artist

def newIdentification(name, id):
    
    identification = {'name': '', 'identification': ''}
    identification['name'] = name
    identification['identification'] = id
    return identification



# Funciones de consulta
def getArtworkbyArtist(catalog, artistname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    posartist = lt.isPresent(catalog['authors'], artistname)
    if posartist > 0:
        artist = lt.getElement(catalog['artist'], posartist)
        return artist
    return None 

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento