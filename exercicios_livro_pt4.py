lista1 = []
lista2 = []

while True:
    valor = input("Qual valor deseja adicionar? ")
    
    if valor == int:
        lista1.append(valor)
    elif valor == "prox":
        print("Indo para a lista 2!")
        continue

    if valor == int:
        lista1.append(valor)
    elif valor == "junta":
        print("Indo para a junção!")
        break

lista3 = (lista1.extend(lista2))

print(lista3,
      lista1,
      lista2,
      )
