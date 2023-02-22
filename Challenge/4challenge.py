import pandas as pd
from colors1 import colors

# Función para cargar los datos desde un archivo csv


def cargar_datos():
    df = pd.read_csv("titanic.csv")
    return df

# Función para mostrar información general del DataFrame


def info_dataFrame(df):
    # Mostrar por pantalla las dimensiones del DataFrame,
    print("\n Dimensiones del DataFrame\n ", df.shape)
    # el número de datos que contiene,
    print("\n Numero de datos: \n ", df.size)
    # los nombres de sus columnas
    print("\n Numero de columnas: \n ", list(df.columns))
    # los nombres de sus filas
    print("\n Numero de filas: \n ", list(df.index))
    # los tipos de datos de las columnas,
    print("\n Tipos de datos de las columnas:\n  ", df.dtypes)
    # las 10 primeras filas
    print("\n Primeras 10 filas\n : ", df.head(10))
    # las 10 últimas filas
    print("\n Ultimas 10 filas: \n ", df.tail(10))


# Función para mostrar información de un pasajero específico
def info_pasajero(df, pasajero):
    pasajero = df.loc[df['PassengerId'] == 148]
    print(pasajero)


def menu():

    print("   ")
    print(colors.terminalBrightBlue("Bienvenidos a los datos del Titanic"))

    print(colors.terminalBrightGreen("   "))
    strs = ('1)  Generar un DataFrame con los datos del fichero.\n'
            '2)  Las dimensiones del DataFrame, el número de datos que contiene,\n'
            '3)  los datos del pasajero con identificador 148.\n'
            '4)  Filas pares del DataFrame.\n'
            '5)  Nombres de las personas de 1ra clase ordenadas alfabéticamente.\n'
            '6)  Porcentaje de personas que sobrevivieron y murieron.\n'
            '7)  Porcentaje de personas que sobrevivieron en cada clase.\n'
            '8)  Eliminar del DataFrame los pasajeros con edad desconocida.\n'
            '9)  Edad media de las mujeres que viajaban en cada clase.\n'
            '10) Añadir una nueva columna definienco a un pasajero menor de edad.\n'
            '11) El porcentaje de menores y mayores de edad que sobrevivieron en cada clase.\n'
            '12) Salir\n'
            '\n'
            '\n')
    print(colors.terminalBrightGreen("  "))

    choice = input(strs + "Seleccione una de las siguientes opciones: ")
    return int(choice)


while True:  # use while True

    choice = menu()
    match choice:
        case 1:
            print("\n")
            print(cargar_datos())
            print("Fichero generado \n")
        case 2:
            print(colors.terminalBrightGray("\n "))
            print(info_dataFrame(cargar_datos()))
        case 3:
            print(colors.terminalBrightGray("\n "))
            pasajero = int(input("¿Que pasajero buscas?: "))
            info_pasajero(cargar_datos(), pasajero)

        case 4:
            print("4 ")
        case 5:
            print("5 ")
        case 6:
            print("6 ")
        case 7:
            print("7 ")
        case 8:
            print("8 ")
        case 9:
            print("9 ")
        case 10:
            print("10 ")
        case 11:
            print("11 ")
        case 12:
            break
    input(colors.terminalBrightRed("\nPresiona enter para continuar."))


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



# Función para cargar los datos desde un archivo csv

def cargar_datos():
    df = pd.read_csv("titanic.csv")
    return df

# Función para mostrar información general del DataFrame


def info_dataframe(df):
    print("Dimensiones del DataFrame:", df.shape)
    print("Número de datos:", df.size)
    print("Nombres de columnas:", list(df.columns))
    print("Nombres de filas:", list(df.index))
    print("Tipos de datos de las columnas:\n", df.dtypes)
    print("Primeras 10 filas:\n", df.head(10))
    print("Últimas 10 filas:\n", df.tail(10))

# Función para mostrar las filas pares del DataFrame


def filas_pares(df):
    pares = df.iloc[::2]
    print(pares)

# Función para mostrar los nombres de las personas en primera clase ordenados alfabéticamente


def nombres_primera_clase(df):
    nombres = df.loc[df['Pclass'] == 1, 'Name'].sort_values()
    print(nombres)

# Función para mostrar porcentajes de supervivencia y muerte


def porcentaje_supervivencia(df):
    total = df['Survived'].count()
    supervivientes = df['Survived'].sum()
    muertos = total - supervivientes
    porcentaje_supervivientes = (supervivientes / total) * 100
    porcentaje_muertos = (muertos / total) * 100
    print("Porcentaje de supervivientes:", porcentaje_supervivientes)
    print("Porcentaje de muertos:", porcentaje_muertos)

# Función para mostrar porcentajes de supervivencia en cada clase


def porcentaje_supervivencia_clase(df):
    total_primera_clase = df.loc[df['Pclass'] == 1, 'Pclass'].count()
    total_segunda_clase = df.loc[df['Pclass'] == 2, 'Pclass'].count()
    total_tercera_clase = df.loc[df['Pclass'] == 3, 'Pclass'].count()

    supervivientes_primera_clase = df.loc[(df['Pclass'] == 1) & (
        df['Survived'] == 1), 'Pclass'].count()
    supervivientes_segunda_clase = df.loc[(df['Pclass'] == 2) & (
        df['Survived'] == 1), 'Pclass'].count()
    supervivientes_tercera_clase = df.loc[(df['Pclass'] == 3) & (
        df['Survived'] == 1), 'Pclass'].count()

    porcentaje_supervivientes_primera_clase = (
        supervivientes_primera_clase / total_primera_clase) * 100
    porcentaje_supervivientes_segunda_clase = (
        supervivientes_segunda_clase / total_segunda_clase) * 100
    porcentaje_supervivientes_tercera_clase = (
        supervivientes_tercera_clase / total_tercera_clase) * 100

    print("Porcentaje de supervivientes en primera clase
    """
