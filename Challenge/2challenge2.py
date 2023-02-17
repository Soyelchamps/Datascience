
numero = int(input("Ingrese un numero para imprimir su tabla de multiplicar: "))

for i in range(0, 10):
    resultado = numero * i
    print(i, " x ", numero, " =", resultado)
