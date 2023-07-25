mes = 1

deposito = int(input("Qual o valor do deposito inicial? "))
taxa_juros = int(input("Qual a taxa de juros da poupança? "))

while mes <= 24:
    novo_deposito = str(input("Vai adicionar algum valor ao deposito? (SIM ou NÃO)  ")).upper()

    if novo_deposito == "SIM":
       deposito = int(input("Qual o valor a ser adicionado? ")) + deposito
    elif novo_deposito == "NÃO":
        print("Nenhum valor depositado")
    else:
        continue #Continua para a proxima iteração sem quebrar o loop

    deposito += deposito * (taxa_juros / 100)
    print(f"No {mes}º mes o lucro foi de R${(deposito / mes):5.2f} totalizando um valor de {deposito:5.2f}")
    mes += 1
