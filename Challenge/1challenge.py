# 1) Imprimir los numeros pares entre 0 y 1000.
for num in range(0, 1001, 2):
    print(num)


# 2) Imprimir los numeros primos entre 0 y 10000.
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# 3) Ingresar un numero e imprimir su tabla de multiplicar. De 0 al 100.
for numero in range(0, 100):
    if es_primo(numero):
        print(numero)


tabla = int(input("Ingrese un numero:"))
for i in range(0, 100):
    resultado = tabla * i
    print(tabla,  "x", i, "= ", resultado)
