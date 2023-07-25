preco_total = 0


while True:
    codigo = int(input("Qual o codigo do produto que deseja comprar?\n"))
    if codigo == 1:
        quantidade = int(input("Qual a quantidade do produto que deseja comprar?\n"))
        preco_total += quantidade * 0.5
    elif codigo == 2:
        quantidade = int(input("Qual a quantidade do produto que deseja comprar?\n"))
        preco_total += quantidade * 1
    elif codigo == 3:
        quantidade = int(input("Qual a quantidade do produto que deseja comprar?\n"))
        preco_total += quantidade * 4
    elif codigo == 5:
        quantidade = int(input("Qual a quantidade do produto que deseja comprar?\n"))
        preco_total += quantidade * 7
    elif codigo == 9:
        quantidade = int(input("Qual a quantidade do produto que deseja comprar?\n"))
        preco_total += quantidade * 8
    elif codigo == 0:
        print(f"O total gasto será: R${preco_total}")
        break
    else:
        print("Código invalido!")