a = int(input())
b = int(input())
a = a + b
b = a - b
a = a - b
print(a)
print(b)

a = int(input())
b = str(a)
suma=0
for i in range(len(b)):
    suma = suma + int(b[i])
print(suma)

import math
print("Введите кофф кв ур")
print("ax^2 + bx + c = 0")
a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")