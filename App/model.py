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
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import quicksort
from DISClib.Algorithms.Sorting import insertionsort
assert cf
import time
from datetime import date

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(listType):
    
    catalog = {'Artwork': None,
               'Artists': None,
               'ArtistsDate': None,
               'ArtworksDateAcquired': None}
    catalog['Artists'] = lt.newList(listType,
                                    cmpfunction=compareartists) 
    catalog['Artwork'] = lt.newList(listType, cmpfunction=compareartworks)
    catalog['ArtistsDate'] = lt.newList(listType, cmpfunction='')
    catalog['ArtworksDateAcquired'] = lt.newList(listType, cmpfunction='')
    #catalog['ArtistTecnique'] = lt.newList(listType, cmpfunction='')

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):

    listArtist = {'DisplayName': artist['DisplayName'],
                'ConstituentID': artist['ConstituentID'],
                'BeginDate': artist['BeginDate'], 
                'EndDate': artist['EndDate'],
                'Nationality': artist['Nationality'],
                'Gender': artist['Gender'],
                'Artworks': lt.newList('ARRAY_LIST')} 
    
    lt.addLast(catalog['Artists'], listArtist)
    
    addArtistDate(catalog, listArtist)

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
                  'URL': artwork['URL'],
                  'Circumference': artwork['Circumference (cm)'],
                  'Depth': artwork['Depth (cm)'],
                  'Diameter': artwork['Diameter (cm)'],
                  'Height': artwork['Height (cm)'],
                  'Length': artwork['Length (cm)'],
                  'Weight': artwork['Weight (kg)'],
                  'Width': artwork['Width (cm)']}
    lt.addLast(catalog['Artwork'], listArtwork)
    artistsID = listArtwork['ConstituentID']
    artistsID = eval(artistsID)

    for a in artistsID:
        addArtworkArtist(catalog, a, listArtwork)
    addArtworkDAcquired(catalog, listArtwork)

def Artistinfo(catalog,artistsID):
    Artistsfound = lt.newList(datastructure='ARRAY_LIST')
    artistsIDList = artistsID.replace('[', '').replace(']', '').split(",")
    print(artistsIDList)
    i=0
    for artist in lt.iterator(catalog["Artists"]):
        if str(artist['ConstituentID']) in artistsIDList:
            lt.addLast(Artistsfound, artist)
            print(i)
            i +=1
        continue
    if lt.size(Artistsfound)>= 1:
        print(Artistsfound)
    
    return Artistsfound





def addArtworkArtist(catalog, artist_id, Artwork):
    
    artists = catalog['Artists']
    posartist = lt.isPresent(artists,artist_id)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
        
    else:
        artist = newArtist(artist_id)
        lt.addLast(artists, artist)
    
    lt.addLast(artist['Artworks'], Artwork)
    

def addArtistDate(catalog, listArtist):
        addDate = newArtistDate(listArtist['DisplayName'], listArtist['BeginDate'], listArtist['EndDate'], listArtist['Nationality'], listArtist['Gender'])
        lt.addLast(catalog['ArtistsDate'], addDate)

def addArtworkDAcquired(catalog, listArtwork):
    addDateAcquired = newArtworksDateAcquired(listArtwork['ObjectID'], listArtwork['Title'], listArtwork['Medium'], listArtwork['Dimensions'], listArtwork['Date'], listArtwork['DateAcquired'], listArtwork['CreditLine'])
    lt.addLast(catalog['ArtworksDateAcquired'], addDateAcquired)

# Funciones para creacion de datos

def newArtist(artistid):
    artist= {'artistID': '',
             'Artworks': None,}
    artist['artistID'] = artistid

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

def newArtworksDateAcquired(ObjectID, artwork, Medium, Dimensions, Date, DateAcquired, CreditLine):
    ArtworkDateAcquired = {'ObjectID': '', 'Title': '', 'ArtistsName': '', 'Medium': '', 'Dimensions': '',
    'Date':'', 'DateAcquired': ''}
    ArtworkDateAcquired['ObjectID'] = ObjectID
    ArtworkDateAcquired['Title'] = artwork 
    #ArtworkDateAcquired['ArtistsName'] = artistname
    ArtworkDateAcquired['Medium'] = Medium 
    ArtworkDateAcquired['Dimensions'] = Dimensions
    ArtworkDateAcquired['Date'] = Date 
    ArtworkDateAcquired['DateAcquired'] = DateAcquired
    ArtworkDateAcquired['CreditLine'] = CreditLine

    return ArtworkDateAcquired

def newTecnique(tecnique):
    artec = {'MediumName': '',
             'Artworks': lt.newList('ARRAY_LIST')}
    artec['MediumName'] = tecnique
    return artec

def subListArtwork(catalog, ListSyze):
    """
    Genera la sublista de Artworks
    """
    ArtworkSample = lt.subList(catalog['Artwork'],1,ListSyze)
    return ArtworkSample

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
        if a['DateAcquired'] != '' and a['DateAcquired']!='0':
            a1 = date.fromisoformat(a['DateAcquired'])
            if a1 >= inicialDate and a1 <= finalDate and a1 != '' and a1!='0':
                lt.addLast(artworksDate, a)
                

    sort_DateAcquired = sortDateAcquired(artworksDate)

    return sort_DateAcquired

def artworksPurchased(sort_DateAcquired):
    count = 0
    for a in lt.iterator(sort_DateAcquired):
        if 'purchase' in a['CreditLine'].lower():
            count += 1
    
    return count


#Req 3:
def getArtistByTecnique(catalog, Artistname):
    ArtistTecnique = lt.newList('ARRAY_LIST', cmpfunction=compATecnique)
    for artists in lt.iterator(catalog['Artists']):
        if artists['DisplayName'] == Artistname:
            for a in lt.iterator(artists['Artworks']):
                tecnique = a['Medium']
                pos = lt.isPresent(ArtistTecnique,tecnique)
                if pos > 0:
                    tec = lt.getElement(ArtistTecnique, pos)
                    lt.addLast(tec['Artworks'], a)
                else:
                    tec = newTecnique(a['Medium'])
                    lt.addLast(ArtistTecnique, tec)
                lt.addLast(tec['Artworks'], a)   
            
    return ArtistTecnique


""""
def addArtworkArtist(catalog, artist_id, Artwork):
    
    artists = catalog['Artists']
    posartist = lt.isPresent(artists,artist_id)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
        
    else:
        artist = newArtist(artist_id)
        lt.addLast(artists, artist)
    
    lt.addLast(artist['Artworks'], Artwork)

    postecnique = lt.isPresent(ArtistTecnique['MediumName'], a['Medium'])
                if postecnique > 0:
                    tec = lt.getElement(ArtistTecnique['MediumName'], postecnique)
                    #lt.addLast(ArtistTecnique['Artworks'], a)
                else:
                    tec = newTecnique(a['Medium'])
                    lt.addLast(ArtistTecnique['MediumName'], a['Medium'])
                lt.addLast(tec['Artworks'], a)
"""


def getArtworksByNationality(catalog):
    nat = lt.newList('ARRAY_LIST')
    for a in lt.iterator(catalog['ArtworksArtist']):
        pass
        
        if a['Nationality'] != '' and a['Nationality']!='0':
            pass

#Req 5
def getArtworkByDepartment(catalog):
    
    for artwork in lt.iterator(catalog['Artwork']):
        pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(a1, a2):
    
    if a1 < int(a2['ConstituentID']):
        return -1
    elif a1 == int(a2['ConstituentID']):
        return 0
    else:
        return 1

def compareartworks(a1, a2):
    if a1['ObjectID'] < a2['ObjectID']:
        return -1
    elif a1['ObjectID'] == a2['ObjectID']:
        return 0
    else:
        return 1

#def cmpartistartowork(o1, o2):
    #if (o1['ObjectID'] < o2['ObjectID']) or (o1['ConstituentID'] < o2['ConstituentID']):
        #return -1
    #elif (o1['ObjectID'] == o2['ObjectID']) and (o1['ConstituentID'] == o2['ConstituentID']):
        #return 0
    #else:
        #return 1

def compareartistID(a1, artist):
    if str(a1) in str(artist['ConstituentID']):
        return 0
    else:
        return -1


def compArtistDate(Artist1, Artist2):
    return (int(Artist1['BeginDate']) < int(Artist2['BeginDate'])) 


def compATecnique(tec, artistTecnique):
    if tec.lower() == artistTecnique['MediumName'].lower():
        return 0
    else:
        return -1 


def comparenationality():
    pass

def compDateAcquired(Date1, Date2):
    if Date1['DateAcquired'] != '' and Date1['DateAcquired'] != '0' and Date2['DateAcquired'] != '0' and Date2['DateAcquired'] != '':
        return (date.fromisoformat(Date1['DateAcquired']) < date.fromisoformat(Date2['DateAcquired']))

def compArtworkTecnique(tecnique1, tecnique2):
    return lt.size(tecnique1['Artworks']) > lt.size(tecnique2['Artworks'])


# Funciones de ordenamiento

def SortDates(DatesArtist):
    #start_time = time.process_time()
    sorted_list = mergesort.sort(DatesArtist, compArtistDate)
    #stop_time = time.process_time()
    #elapsed_time_mseg = (stop_time - start_time)*1000 
    return sorted_list

def sortDateAcquired(artworksDate):
    
    #start_time = time.process_time()
    sorted_list = mergesort.sort(artworksDate, compDateAcquired)
    #stop_time = time.process_time()
    #elapsed_time_mseg = (stop_time - start_time)*1000
        
    return sorted_list

def sortArtworkTecnique(ArtistTecnique):
    sort_list = mergesort.sort(ArtistTecnique, compArtworkTecnique)
    return sort_list
    
    