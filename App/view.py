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

catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()

        controller.loadData(catalog)

        print('Obras de arte cargados: ' + str(lt.size(catalog['Artwork'])))
        print('Artistas cargados: ' + str(lt.size(catalog['Artists'])))
        i = -1
        print('Últimas tres obras: ')
        while i > -4:
            print(str(catalog['Artwork']['elements'][i]))
            i-=1
        j = -1
        print('Últimos tres artistas: ')
        while j > -4:
            print(str(catalog['Artists']['elements'][i]))
            j-=1


    elif int(inputs[0]) == 2:
        anoInicial = input('Ingresa el año inicial del rango: ')
        anoFinal = input('Ingrese el año final del rango: ')


    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    
    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass


    else:
        sys.exit(0)
sys.exit(0)
