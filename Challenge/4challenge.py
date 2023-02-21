import pandas as pd
from colors1 import colors

print("   ")
print(colors.terminalBrightBlue("Bienvenidos a los datos del Titanic"))
print("   ")
print(colors.terminalBrightGreen("Seleccione una de las siguientes opciones:"))
print(colors.terminalBrightGreen("Para finalizar escriba 'SALIR' o 'S'"))
print("   ")

"""
print(colors.terminalMagenta("1) Generar un DataFrame con los datos del fichero."))
print(colors.terminalMagenta("2) Las dimensiones del DataFrame"))
print(colors.terminalMagenta(
    "3) Los datos del pasajero con identificador 148."))
print(colors.terminalMagenta(
    "4) Las filas pares del DataFrame."))
print(colors.terminalMagenta(
    "5) Los nombres de las personas que iban en primera clase ordenadas alfabéticamente."))
print(colors.terminalMagenta(
    "6) El porcentaje de personas que sobrevivieron y murieron."))
print(colors.terminalMagenta(
    "8) Eliminar del DataFrame los pasajeros con edad desconocida."))
print(colors.terminalMagenta(
    "9) La edad media de las mujeres que viajaban en cada clase."))
print(colors.terminalMagenta(
    "10) Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no."))
print(colors.terminalMagenta(
    "11) El porcentaje de menores y mayores de edad que sobrevivieron en cada clase."))
print(colors.terminalMagenta(
    "12) SALIR"))


print("   ")
seleccion = input(colors.terminalGray("Selecciona tu opcion: "))

"""


def menu():
    strs = ('Enter 1 for addition\n'
            'Enter 2 for subtaction\n'
            'Enter 3 for multiplication\n'
            'Enter 4 for division\n'
            'Enter 5 to exit : ')
    choice = input(strs)
    return int(choice)


while True:  # use while True
    choice = menu()
    match choice:
        case 1:
            print(" ")
        case 2:
            print(" ")
        case 3:
            print(" ")
        case 4:
            print(" ")
        case 5:
            print(" ")
        case 6:
            print(" ")
        case 7:
            print(" ")
        case 8:
            break
"""
El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:

1) Generar un DataFrame con los datos del fichero.
2) Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
3) Mostrar por pantalla los datos del pasajero con identificador 148.
4) Mostrar por pantalla las filas pares del DataFrame.
5) Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
6) Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
7) Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
8) Eliminar del DataFrame los pasajeros con edad desconocida.
9) Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
10) Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
11) Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
"""
