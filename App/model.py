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
from DISClib.Algorithms.Sorting import mergesort as sa
assert cf

from datetime import date

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(listType):
    
    catalog = {'Artwork': None,
               'Artists': None,
               'artworkArtist': None,
               'ArtistsDate': None,
               'ArtworksDateAcquired': None}

    catalog['Artwork'] = lt.newList(listType)
    catalog['Artists'] = lt.newList(listType,
                                    cmpfunction=compareartists) 
    catalog['artworkArtist'] = lt.newList(listType, cmpfunction='')
    catalog['ArtistsDate'] = lt.newList(listType, cmpfunction='')
    catalog['ArtworksDateAcquired'] = lt.newList(listType, cmpfunction='')

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):

    listArtist = {'DisplayName': artist['DisplayName'],
                'ConstituentID': artist['ConstituentID'],
                'BeginDate': artist['BeginDate'], 
                'EndDate': artist['EndDate'],
                'Nationality': artist['Nationality'],
                'Gender': artist['Gender'],
                'ArtistBio': artist['ArtistBio'],
                'Wiki QID': artist['Wiki QID'],
                'ULAN': artist['ULAN'],
                'Artworks': lt.newList('ARRAY_LIST')} #artist['DisplayName'] == aaa
                                                      #artist['Artoworks']['Medium']
    
    lt.addLast(catalog['Artists'], listArtist)
    addArtistDate(catalog,listArtist)

def addArtwork(catalog, artwork):

    listArtwork = {'ObjectID': artwork['ObjectID'], 
                  'Title': artwork['Title'],
                  'ConstituentID': artwork['ConstituentID'],
                  'Date': artwork['Date'],
                  'Medium': artwork['Medium'],
                  'Dimensions': artwork['Dimensions'],
                  'CreditLine': artwork['CreditLine'],
                  'Department': artwork['Department'],
                  'DateAcquired': artwork['DateAcquired'],
                  'URL': artwork['URL']}
 
    lt.addLast(catalog['Artwork'], listArtwork)

    #artistID = listArtwork['ConstituentID'].split(',') 

    #for a in artistID:
        #addArtworkArtist(catalog, artwork, artistID[1:-1])
        
def addArtworkArtist(catalog, artist_id, artwork):
    artists = catalog['ArtworkArtist']
    posartist = lt.isPresent(artists,artist_id)
    if posartist > 0:
        artist = newArtist(artist_id)
    else:
        artist = newArtist(artist_id)
        lt.addLast(artists, artist)
    lt.addLast(artist['ArtworkArtist'], artwork)


def addArtistDate(catalog, listArtist):
        addDate = newArtistDate(listArtist['DisplayName'], listArtist['BeginDate'], listArtist['EndDate'], listArtist['Nationality'], listArtist['Gender'], listArtist['ArtistBio'], listArtist['Wiki QID'], listArtist['ULAN'])
        lt.addLast(catalog['ArtistsDate'], addDate)

def addArtworkDAcquired(catalog, listArtwork):
    addDateAcquired = newArtworksDateAcquired(listArtwork['ObjectID'], listArtwork['Title'], listArtwork['Medium'], listArtwork['Dimensions'], listArtwork['Date'], listArtwork['DateAcquired'], listArtwork['URL'])
    lt.addLast(catalog['ArtworksDateAcquired'], addDateAcquired)



# Funciones para creacion de datos

def newArtist(artistid):
    artist= {'artistID': '',
             'Artworks': None,}
    artist['artistID'] = artistid

    artist['Artworks'] = lt.newList('ARRAY_LIST')

    return artist

def newArtistDate(artist, BeginDate, EndDate, nationality, gender, Artistbio, Wiki, ULAN):
    artistDate = {'Name': '', 'BeginDate': '', 'EndDate': '', 'Nationality': '', 'Gender': '', 'ArtistBio': '', 'Wiki QID': '', 'ULAN': ''}
    artistDate['Name'] = artist
    artistDate['BeginDate'] = BeginDate
    artistDate['EndDate'] = EndDate
    artistDate['Nationality'] = nationality
    artistDate['Gender'] = gender
    artistDate['ArtistBio'] = Artistbio
    artistDate['Wiki'] = Wiki
    artistDate['ULAN'] = ULAN

    return artistDate

def newArtworksDateAcquired(ObjectID, artwork, Medium, Dimensions, Date, DateAcquired, URL):
    ArtworkDateAcquired = {'ObjectID': '', 'Title': '', 'ArtistsName': '', 'Medium': '', 'Dimensions': '',
    'Date':'', 'DateAcquired': '', 'URL':''}
    ArtworkDateAcquired['ObjectID'] = ObjectID
    ArtworkDateAcquired['Title'] = artwork 
    #ArtworkDateAcquired['ArtistsName'] = Artistname
    ArtworkDateAcquired['Medium'] = Medium 
    ArtworkDateAcquired['Dimensions'] = Dimensions
    ArtworkDateAcquired['Date'] = Date 
    ArtworkDateAcquired['DateAcquired'] = DateAcquired
    ArtworkDateAcquired['URL'] = URL 

    return ArtworkDateAcquired

# Funciones de consulta

def getArtistByDate(catalog, BeginDate, EndDate):

    
    DatesArtist = lt.newList('ARRAY_LIST')

    for a in lt.iterator(catalog['ArtistsDate']): 
        if int(a['BeginDate']) >= BeginDate and int(a['BeginDate']) <= EndDate and a['BeginDate'] != "" and a['BeginDate'] != 0:
            lt.addLast(DatesArtist, a)

    Dates_Artist = SortDates(DatesArtist)

    return Dates_Artist 

def artworksByDate(catalog, inicial, final):

    artworksDate = lt.newList('ARRAY_LIST')

    inicialDate = date.fromisoformat(inicial)
    finalDate = date.fromisoformat(final)

    for a in lt.iterator(catalog['ArtworksDateAcquired']):
        print(a['DateAcquired'])
        a1 = date.fromisoformat(a['DateAcquired'])
        if a1 >= inicialDate and a1 <= finalDate and a1 != '' and a1!='0':
            print(a)
            lt.addLast(artworksDate, a)

    sort_DateAcquired = sortDateAcquired(artworksDate)

    return sort_DateAcquired


def ArtistByTecnique(catalog, artist):
    pass

    

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists():
    pass

def compArtistDate(Artist1, Artist2):
    return (int(Artist1['BeginDate']) < int(Artist2['BeginDate'])) 


def comparetecnique():
    pass

def comparenationality():
    pass

def compDateAcquired(Date1, Date2):
    return (date.fromisoformat(Date1['BeginDate']) < date.fromisoformat(Date2['BeginDate']))

# Funciones de ordenamiento

def SortDates(DatesArtist):
    sorted_list = sa.sort(DatesArtist, compArtistDate)
    return sorted_list

def sortDateAcquired(artworksDate):
    sorted_list = sa.sort(artworksDate, compDateAcquired)
    return sorted_list