entradas = []

while True:
    entrada = int(input("Digite qualquer numero pra continuar, ou 0 para sair:\n"))

    if entrada == 0:
        print(f"Você digitou um total de {  i ::(entradas)} numeros")
        print(f"A soma total dos numeros digitados é: {sum(entradas)}, "
              f"E a média é igual a {(sum(entradas) / len(entradas)):5.1f}")
        break
    else:
        entradas.append(int(entrada))
        print(f"Lista de entradas: {entradas}")
