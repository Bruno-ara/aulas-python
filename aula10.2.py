
n = input("Usuário: ")
c = 3
for x in range(1, 4):
    s = int(input("Digite sua senha: "))
    c -= 1
    if s == 123456:
        print(f"Olá, {n}. Seja bem-bindo ao nosso banco!")
        break
    if c > 0:
        print(f"Senha incorreta! Você ainda tem {c} tentativa.")
    else:
        print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossso caixas.")
