from math import sqrt
a = float(input("O valor de A: "))
b = float(input("O valor de B: "))
c = float(input("O valor de C: "))
delta = b*b - 4*a*c
if delta == 0:
    x = -b / (2*a)
elif delta > 0:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print('''X1 = {}
X2 = {}'''.format(x1, x2))
else:
    print("Não existe raíz real.")
