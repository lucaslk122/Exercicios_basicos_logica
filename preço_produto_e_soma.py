
produto1 = []
produto2 = []
produto_codigo1 = int(input("digite o código do produto 1: "))
produto1.append(produto_codigo1)
produto_quantidade1 = int(input("digite a quantidade de produto 1: "))
produto1.append(produto_quantidade1)
produto_preço_produto1 = float(input("digite o preço do produto 1: "))
produto1.append(produto_preço_produto1)
produto_codigo2 = int(input("digite o código do produto 2: "))
produto2.append(produto_codigo2)
produto_quantidade12 = int(input("digite a quantidade de produto 2: "))
produto2.append(produto_quantidade12)
produto_preço_produto2 = float(input("digite o preço do produto 2: "))
produto2.append(produto_preço_produto2)
x = produto1[1] * produto1[2]
y = produto2[1] * produto2[2]
z = x + y
print("O valor a pagar é R$",z,"reais")