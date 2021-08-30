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

    elif int(inputs[0]) == 2:
        anoInicial = input('Ingrese el año inicial: ')
        anoFinal = input('Ingrese el año final: ')

        print("Número total de artistas en el rango de año: ")
        print("Primeros 3 y últimos 3 artistas del rango cronológico: ")
        print("Nombre del artista: ")
        print("Año de nacimiento del artista: ")
        print("Nscionalidad: ")
        print("Género: ")

    elif int(inputs[0]) == 3:
        anioInicial= input('Ingrese el año inicial: ')
        mesInicial= input('Ingrese el mes de la fecha inical: ')
        diaInicial = input('Ingrese el dia de la fecha inicial: ')
        anioFinal = input('Ingrese el año final: ')
        mesFinal=input('Ingrese el mes de la fecha final: ')
        diaFinal = input('Ingrese el dia de la fecha final: ')

        print("Número total de obras en el rango cronológico: ")
        print("Número total de obras adquiridas por compra ('purchase...'): ")
        print("Primeras 3 y últimas 3 obras del rango: ")
        print("Título de la obra: ")
        print("Artista(s) de la obra: ")
        print("Fecha de la obra: ")
        print("Medio: ")
        print("Dimensiones: ")

    elif int(inputs[0]) == 4:
        artista= input('Ingrese el nombre del artista: ')

        print("Total de obras: ")
        print("Total técnias (medios) utilizados: ")
        print("La técnica más utlizada: ")
        print("El listado de las obras de dicha técnica: ")
        print("Titulo de la obra: ")
        print("Fecha de la obra: ")
        print("Medio: ")
        print("Dimensiones: ")

    
    elif int(inputs[0]) == 5:
        obras= input('Ingrese las obras del museo: ')

        print("Lista de nacionalidades ordenadas por el total de obras de mayor a menor: ")
        print("Información de las obras de la nacionalidad con el mayor número de obras: ")
        print("Titulo de la obra: ")
        print("Artista(s): ")
        print("Fecha de la obra: ")
        print("Medio: ")
        print("Dimensiones: ")

    elif int(inputs[0]) == 6:
        departamento= input('Ingrese el departamento del museo: ')

        print("Total de obras para transportar: ")
        print("Precio estimado del servicio en USD: ")
        print("5 obras más antigua a transportar: ")
        print("5 obras más costosas para transportar: ")
        print("Título de la obra: ")
        print("Artista(s): ")
        print("Clasificación: ")
        print("Fecha de la obra: ")
        print("Medio: ")
        print("Dimensiones: ")
        print("Costo asociado al transporte: ")


    else:
        sys.exit(0)
sys.exit(0)
