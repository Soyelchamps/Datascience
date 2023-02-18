# Lambda function: Is a reserved word for using to create shorter version of function.

# lambda arguments :expresion
def sum(n1, n2):
    return n1+n2


def sum_example(n1, n2): return n1 + n2


def sum_example(n1, n2): return n1 + n2


def main_function(param):
    return lambda param2: param2 * param


"""
table_two = main_function(2)
print(table_two(1))
print(table_two(2))
print(table_two(3))
print(table_two(4))

table_tree = main_function(3)
print(table_tree(1))
print(table_tree(2))
print(table_tree(3))
print(table_tree(4))

"""
tabla = int(input("¿ que tabla quieres calcular? : "))

table_of = main_function(tabla)

print("Aqui esta la tabla del: ", tabla)
for i in range(1, 11):
    print(tabla, "x", i, "=", table_of(i))

# for i in range(0, 10):
 #   print("Tabel x 2", i, "x", table_two(i))
  #  print("Table 3", table_tree(i))
# print(sum(1, 2))
# print(sum_example(1, 2))
