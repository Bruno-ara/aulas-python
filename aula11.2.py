produtos = []
while True:
    nome_produto = input("nome do produto: ")
    produtos.append(nome_produto)
    esc = input("deseja continuar? [S|N]").upper()
    if esc == "N":
        break
print("Sua lista de produtos: ", produtos)
