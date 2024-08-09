pt = int(input("Primeiro termo: "))
qt = int(input("Quantidade de termos: "))
r = int(input("Razão: "))
s = 0 
ut = pt + (qt - 1)*r
for x in range(pt, ut + 1, r):
    s += x
print(s)
