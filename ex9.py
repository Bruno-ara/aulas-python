t = float(input("Digite o preço total da venda: "))
cod = int(input('''
---Código---
1. à vista (espécie)
2. cartão de débito
3. cartaõ de crédito (vencimento)
Código do pagamento: '''))
if cod == 1:
    print("o novo valor será R${:.2f}".format(t * 0.85))
elif cod == 2:
    print("o novo valor será R${:.2f}".format(t * 0.9))
elif cod == 3:
    print("o novo valor será R${:.2f}".format(t * 0.95))
else:
    print("Opção inválida, tente nvoamente.")
