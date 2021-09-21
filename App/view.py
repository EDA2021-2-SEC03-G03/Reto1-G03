"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time

defaul_time = 1000
sys.setrecursionlimit(defaul_time*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista cronológica de los artistas")
    print("3- Lista cronológica de adquisiciones")
    print("4- Calsificación de obras de un artista por técnica")
    print("5- Clasificar obras por la nacionalidad de sus creadores")
    print("6- Transporte de obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")

catalog = None

#funciones de print


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        listType = input('Ingrese el tipo de lista que quiere implementar (ARRAY_LIST o LINKED_LIST): ').upper()
        catalog = controller.initCatalog(listType)

        controller.loadData(catalog)

        print('Obras de arte cargados: ' + str(lt.size(catalog['Artwork'])))
        print('Artistas cargados: ' + str(lt.size(catalog['Artists'])))
        print("Last three artworks:")
        print(catalog['Artwork']['elements'][-3:])
        print("Last three artists:")
        print(catalog['Artists']['elements'][-3:])
        
        
        
        
    elif int(inputs[0]) == 2:
        
        #Req1: 
        anoInicial = int(input('Ingresa el año inicial del rango: '))
        anoFinal = int(input('Ingrese el año final del rango: '))
        DatesA = controller.getArtistByDate(catalog, anoInicial, anoFinal)
        print("Tiempo utilizado en el ordenamiento: " + str(DatesA[1]) + " Milisegundos" )
        print('There are ' + str(lt.size(DatesA[0])) + ' artists born between ' + str(anoInicial) + ' and ' + str(anoFinal))
        i=1
        print("First three artists:")
        while i < 4:
            print(str(lt.getElement(DatesA[0], i)))
            i+=1
        j = -2
        print("Last three artists: ")
        while j < 1:
            print(str(lt.getElement(DatesA[0], j)))
            j+=1
        


    elif int(inputs[0]) == 3:
        
        #ordi = controller.sortDateArtwork(catalog, ordenamiento, ListSyze)
        #print("Tiempo utilizado en el ordenamiento: " + str(ordi[1]) + " Milisegundos " + " con un tamaño de muestra de " + str(ListSyze))
        #print("Para la muestra de", ListSyze, " elementos, el tiempo (mseg) es: ", str(ordi[0]))
        #Req2:
        Inicial = input('Ingresa la fecha inicial del rango, en el formato AAAA-MM-DD: ')
        Final = input('Ingrese la fecha final del rango, en el formato AAAA-MM-DD: ')
        datesArtworks = controller.getArtworksByDateAcquired(catalog, Inicial, Final)
        print('The MoMA acquired ' + str(lt.size(datesArtworks)) + ' unique pieces between ' + Inicial + ' and ' + Final)
        print('And purchased ' + str(controller.getartworkPurchased(datesArtworks)) + ' of them.')
        print("First three elements: ")
        print(datesArtworks['elements'][0:3])
        print("Last three elements: ")
        print(datesArtworks['elements'][-3:])

    elif int(inputs[0]) == 4:
        #Req 3:
        Artist = input('Ingrese el nombre del artista: ')
        ArtworkTecnique = controller.getArtistByTecnique(catalog, Artist)
        print(ArtworkTecnique)

        #print(' with MoMA ID ' + ' has ' + ' pieces in his/her name at the museum.')
        #print('There are ' + ' different mediums/tecniques in his/her work.')


        #print('His/Her most used Medium/Tecnique is ' + ' with ' + ' pieces')
        #print('A sample of ' + ' from the collection are:')
       
        

    
    elif int(inputs[0]) == 5:
        #Req4: 
        DatesA = controller.getArtworksByNationality(catalog)

    elif int(inputs[0]) == 6:
        #Req5:
        dep = input('Ingrese el departamento del museo: ')

        print('The MoMA is going to transport ' + ' artifacts from Drawings and Prints')
        print("REMEMBER! NOT all MoMA's data is complete!!!... These are estimates.")
        print("Estimated cargo weight (kg): ")
        print("Estimated cargo cost (USD): ")

        print("--------------------------------------------------------------------------")
        print("Top 5 oldest artworks to transport: ")
        print("--------------------------------------------------------------------------")
        print("Top 5 most expensive artworks to transport: ")

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
