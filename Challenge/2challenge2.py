# 1) Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
div = ""

while div != "Exit":
    div = input("¿Que divisa buscas? ")

    Encontrada = False
    for k, v in divisas.items():
        if div == k:
            print("Divisa", k, "Simbolo", v)
            Encontrada = True
    if Encontrada == False and div != "Exit":
        print("La divisa no fue encontrada")
        R = input("¿Deseas agregarla? S/N: ").lower()
        if R == "s":
            Simbolo = input("Agrega el simbolo de : ")
            divisas[div] = Simbolo
        else:
            print("Fue un placer atenderle")


# print("El simbolo de la divisa es: ", divisas)

# 2)Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# 3)Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media.

# 4)Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

# 5)Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
