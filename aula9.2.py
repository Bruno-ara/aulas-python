pt = int(input("Primeiro termo: "))
qt = int(input("Quantidade de termos: "))
r = int(input("Razão: "))
s = 0 
for x in range(pt, qt + 1, r):
    s += x
print(s)
