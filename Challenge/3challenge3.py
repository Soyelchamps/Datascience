# Ejercicio 1
# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

# Define funcion
def mas_larga(cadena):
    # Inicializa variable longitud log
    log = 0
    # Recorre todo el arreglo de la
    for i in range(len(cadena)):
        # si la loonigtud de la palabra es mayor a la variable longitud
        if len(cadena[i]) > log:
            # reemplaza el valor longitud
            log = len(cadena[i])
            # actualiza la palabra mas larga
            palabra = cadena[i]
        # retonrna la palabra
    return palabra


# Cadena que se crea
cadena = ["Delia", "CarlosDIAZBARRIAG", "Angel", "Ricardo"]
# imprime el resulado de la funcion
print(mas_larga(cadena))

"""


Ejercicio 2
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

Ejercicio 3
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

Ejercicio 4
Construir un pequeño programa que convierta números binarios en enteros.

Ejercicio 5
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""
