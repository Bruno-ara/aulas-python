s = m = mn = pr = 0
mnn = ""
nm = input("noem: ")
pr = float(input("preço: "))
mn = pr
for x in range(1, 5):
    nm = input("noem: ")
    pr = float(input("preço: "))
    s += pr
    m += 1
    if pr < mn:
        pr = mn
        nm = mnn
print(f"Média aritimética{s / m}, nome do remédio de menor preço {mnn} e preço do remédio {mn}")
