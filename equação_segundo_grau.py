
import math
a = float(input("Dgite o valor de a(não pode ser 0): "))
b = float(input("Dgite o valor de b: "))
c = float(input("Dgite o valor de c: "))
if a == 0:
    print("Não pode ser 0, digite novamente:")
    a = a = float(input("Dgite o valor de a(não pode ser 0): "))
delta = (math.pow(b,2)) - (4*a*c)
if delta < 0:
    print("A equação não possui valores reais, pois o delta é negativo!")
else:
    x1 = (-b - math.sqrt(delta)) / 2*a
    x2 = (-b + math.sqrt(delta)) / 2*a
    print(f"A equação possui razes {x1} e {x2}")