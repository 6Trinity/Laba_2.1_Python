import math
A = float(input("Введите сторону a"))
B = float(input("Введите сторону b"))
C = float(input("Введите сторону c"))
P = float((A + B + C)/2)
S = math.sqrt(P*(P - A)*(P - B)*(P - C))
print("Площадь треугольника: {0}".format(S))
