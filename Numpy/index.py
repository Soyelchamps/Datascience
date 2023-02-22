import numpy as np
import matplotlib.pyplot as plt
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0.1, 0.3, 3])
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0.1, 0.3, 3])
print(a)
# print(type(a))

a.sort()
print(a)

mean = a.mean()

print(mean)
max = a.max()
min = a.min()
print(max)
print(min)

c = np.concatenate((a, b))
print("")
print("")
print("")
c.sort()
print(c)

print("Dimensiones")
print(a.ndim)
print(b.ndim)


print("Tamaño")
print("a = ", a.size)
print("b = ", b.size)
print("c = ", c.size)
d = np.array([[[1, 2, 3], [3, 4, 5,]], [[1, 2, 3],
             [3, 4, 5,]], [[1, 2, 3], [3, 4, 5,]]])
print("Forma\n")
print("a = ", a.shape)
print("b = ", b.shape)
print("c = ", c.shape)
print("d = ", d.shape)

e = np.array([[[1, 2, 4, 6], [1, 3, 45, 5]]])
# f[1,3,4,5]=f[3]


print(" \n")
print(" \n")
print(" \n")
""""
print(e[0][1][2])
print("e = ", d.size)
for i in range(1):
    for j in range(2):
        for k in range(4):
            print(e[i][j][k])
"""
for x in np.nditer(e, flags=['buffered']):
    print(x)

"""
print(" \n")
print(" \n")
print(" \n")
print(" \n")
for i in range(1):
    for j in range(2):
        if (j != 0):
            for k in range(4):
                print(e[i][j][k])
"""
print(" \n")
print(" \n")
print(" \n")
print(" \n")

print(e)

for x in np.nditer(e[:, :, 0::3]):
    print(x)

print(a)
for idx, x in np.ndenumerate(e):
    print("idx = ", idx, " x = ", x)

print("a= ", a)
plt.plot(a)
plt.show()
