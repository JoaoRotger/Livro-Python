exercicio = False


# EXERCICIO 1

def soma(n1, n2):
    print(n1 + n2)


def subtracao(n1, n2):
    print(n1 - n2)


def multiplicacao(n1, n2):
    print(n1 * n2)


def divisao(n1, n2):
    print(n1 / n2)


def calculadora(n1, n2):
    operacao = False
    while not operacao:
        print('''
        ####################################################################################################################
        Que conta você quer fazer?
        1) Soma
        2) Subtração
        3) Multiplicação
        4) Divisão
        5) Sair
    
        IMPORTANTE: Todos os exercicios foram retirados do livro Introdução a Programação com Python, pagina 83.
        ####################################################################################################################
        ''')
        operacao = int(input("Digite o numero do exercicio que deseja ver: "))

        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))

        if operacao == 1:
            soma(numero1, numero2)
        elif operacao == 2:
            subtracao(numero1, numero2)
        elif operacao == 3:
            multiplicacao(numero1, numero2)
        elif operacao == 4:
            divisao(numero1, numero2)
        elif operacao == 5:
            exit(0)
        else:
            print("Opção invalida, digite de novo")
        operacao = False


########################################################################################################################

# EXERCICIO 2

def emprestimo():
    valor_casa = int(input("Qual o valor da casa a ser comprada? "))
    valor_salario = int(input("Qual o seu salario? "))
    anos_a_pagar = int(input("Por quantos anos deseja pagar? "))
    salario_30 = valor_salario * 0.30
    prestacao = (valor_casa / (anos_a_pagar * 12)) < salario_30
    if prestacao:
        print(f"O valor da prestação será de R${prestacao} por mês!")


########################################################################################################################

# EXERCICIO 3

def energia():
    kwh = int(input("Quantos kWh foram consumidos? "))
    tipo = str(input("Qual o tipo de instalção? (R para residencias, C para comercial, e I para industrias) ")).upper()
    preco = 0
    if tipo == "R":
        if kwh <= 500:
            preco = 0.40 * kwh
        else:
            preco = 0.65 * kwh
    elif tipo == "C":
        if kwh <= 1000:
            preco = 0.55 * kwh
        else:
            preco = 0.6 * kwh
    elif tipo == "I":
        if kwh <= 5000:
            preco = 0.55 * kwh
        else:
            preco = 0.6 * kwh
    print(f"O preço é de  R${preco}!")


########################################################################################################################


while not exercicio:
    print('''
    ####################################################################################################################
    Que conta você quer fazer?
    1) Exercicio 1
    2) Exercicio 2
    3) Exercicio 3
    4) Sair

    IMPORTANTE: Todos os exercicios foram retirados do livro Introdução a Programação com Python, pagina 83.
    ####################################################################################################################
    ''')
    exercicio = int(input("Digite o numero do exercicio que deseja ver: "))

    if exercicio == 1:
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))
        calculadora(numero1, numero2)
    elif exercicio == 2:
        emprestimo()
    elif exercicio == 3:
        energia()
    elif exercicio == 5:
        exit(0)
    else:
        print("Opção invalida, digite de novo")
    exercicio = False
