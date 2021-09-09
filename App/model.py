﻿"""
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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    
    catalog = {'Artwork': None,
               'Artists': None,
               'artworkArtist': None,
               'ArtistsDate': None}

    catalog['Artwork'] = lt.newList('ARRAY_LIST')
    catalog['Artists'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareartists) 
    catalog['artworkArtist'] = lt.newList('ARRAY_LIST', cmpfunction='')
    catalog['ArtistsDate'] = lt.newList('ARRAY_LIST', cmpfunction='')

    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):

    listArtwork = {'ObjectID': artwork['ObjectID'], 
                  'Title': artwork['Title'],
                  'ConstituentID': artwork['ConstituentID'],
                  'Date': artwork['Date'],
                  'Medium': artwork['Medium'],
                  'Dimensions': artwork['Dimensions'],
                  'CreditLine': artwork['CreditLine'],
                  'Department': artwork['Department'],
                  'DateAcquired': artwork['DateAcquired']}
 
    lt.addLast(catalog['Artwork'], listArtwork)

    #artistID = listArtwork['ConstituentID'].split(',') 

    #for a in artistID:
        #addArtworkArtist(catalog, artwork, artistID[1:-1])
        

def addArtist(catalog, artist):

    #artist = catalog['Artists']

    listArtist = {'DisplayName': artist['DisplayName'],
                'ConstituentID': artist['ConstituentID'],
                'BeginDate': artist['BeginDate'], 
                'EndDate': artist['EndDate'],
                'Nationality': artist['Nationality'],
                'Gender': artist['Gender'], 
                'Artworks': lt.newList('ARRAY_LIST')} #artist['DisplayName'] == aaa
                                                      #artist['Artoworks']['Medium']

    addArtistDate(catalog, artist['DisplayName'], artist['BeginDate'], artist['EndDate'], artist['Nationality'], artist['Gender'])
    
    lt.addLast(catalog['Artists'], listArtist)




def addArtistDate(catalog, artist, BeginDate, EndDate, nationality, gender):
    if int(BeginDate) != 0:
        addDate = newArtistDate(artist, BeginDate, EndDate, nationality, gender)

        lt.addLast(catalog['ArtistsDate'], addDate)



# Funciones para creacion de datos

def newArtist(artistname):
    artist= {'artistID': '',
             'Artworks': None,}
    artist['artistID'] = artistname

    artist['Artworks'] = lt.newList('ARRAY_LIST')

    return artist

def newArtistDate(artist, BeginDate, EndDate, nationality, gender):
    artistDate = {'Name': '', 'BeginDate': '', 'EndDate': '', 'Nationality': '', 'Gender': ''}
    artistDate['Name'] = artist
    artistDate['BeginDate'] = BeginDate
    artistDate['EndDate'] = EndDate
    artistDate['Nationality'] = nationality
    artistDate['Gender'] = gender

    return artistDate

# Funciones de consulta

def getArtistByDate(catalog, BeginDate, EndDate):

    
    DatesArtist = lt.newList('ARRAY_LIST')

    for a in lt.iterator(catalog['ArtistsDate']): 
        
        if int(a['BeginDate']) >= BeginDate and int(a['BeginDate']) <= EndDate:
            lt.addLast(DatesArtist, a)

    Dates_Artist = SortDates(DatesArtist)

    return Dates_Artist 

def ArtistByTecnique(catalog, artist):
    pass

    

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists():
    pass

def compArtistDate(Artist1, Artist2):

    return int(Artist1['BeginDate'])< int(Artist2['BeginDate'])


#def compareartist_ID():
    #pass

#def compareartwork_ID():
    #pass

def comparetecnique():
    pass

def comparenationality():
    pass

# Funciones de ordenamiento

def SortDates(DatesArtist):
    sa.sort(DatesArtist, compArtistDate)