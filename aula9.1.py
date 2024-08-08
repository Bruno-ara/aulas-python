a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
t = 0
if a < b:
    for x in range(a, b):
        t += x
    print(t)
else:
    print("Erro")
