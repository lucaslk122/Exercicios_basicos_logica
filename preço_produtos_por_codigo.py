print("Lanchonete do Lucão, seja bem vindo")
print("""Possuimos alguns produtos, a seguir está o código,o produto e o preço:
    [1] Cachorro quente - R$4.00
    [2] X-Salada - R$4.50
    [3] X-Tudo - R$8.50
    [4] X - Super lanche super Vegan - R$5.00
    [5] Refrigerante - R$1.50
""")
opção = int(input("Opção desejada: "))
if opção == 1:
    quantidade1 = int(input("Digite a quantidade: "))
    valor = quantidade1 *4.00
    print(f"Valor a ser é R${valor}")
elif opção == 2:
    quantidade2 = int(input("Digite a quantidade: "))
    valor1 = quantidade2 *4.50
    print(f"Valor a ser é R${valor1}")
elif opção == 3:
    quantidade3 = int(input("Digite a quantidade: "))
    valor2 = quantidade3 *8.50
    print(f"Valor a ser é R${valor2}")
elif opção == 4:
    quantidade4 = int(input("Digite a quantidade: "))
    valor3 = quantidade4 *5.00
    print(f"Valor a ser é R${valor3}")
elif opção == 5:
    quantidade5 = int(input("Digite a quantidade: "))
    valor4 = quantidade5 *1.50
    print(f"Valor a ser é R${valor4}")
else:
    print("Esse código não existe, tente novamente")