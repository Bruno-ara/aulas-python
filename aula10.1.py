mb =""
pm = float("inf")
sp  = 0
for x in range(5):
    medicamento = input("Digite o nome do medicamente>:")
    preco = float(input("Digeite o repço"))

    if preco < pm:
        pm = preco
        mb = medicamento
    sp += preco
media = sp / 5
print(f"nome: {mb}; preco {pm}; media {media}")
