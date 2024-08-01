print('''Apresentadores dos jornais:
Zé Pinheiro e Ana Carla Araújo - Bom dia Nação
Bill Bonner e Carla Vasconcelos - Jornal Brasileiro''')
s = input("Flouti: ").lower()
if s == "pinheiro" or s == "araujo":
    print("Bom dia Nação")
elif s == "bonner" or s == "vasconcelos":
    print("Jornal Brasileiro")
else:
    print("Apresentador nao achado")
