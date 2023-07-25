pergunta = False


def soma_numeros():
    primeiro_numero = int(input("Digite o primeiro numero:\n"))
    segundo_numero = int(input("Digite o segundo numero:\n"))
    numeros_soma = primeiro_numero + segundo_numero
    print(f"A soma de {primeiro_numero} + {segundo_numero} é igual a {numeros_soma}")


def conversor_metros():
    tamanho_metros = float(input("digite o valor em metros:\n"))
    milimetros = tamanho_metros * 1000
    print(f"{tamanho_metros} é igual a {milimetros} em milimetros.")


def conversor_segundos():
    quant_dias = int(input("Quantos dias?\n"))
    quant_horas = int(input("Quantas horas?\n"))
    quant_minutos = int(input("Quantos minutos?\n"))
    total_segundos = (quant_dias * 86400) + (quant_horas * 3600) + (quant_minutos * 60)
    print(f"{quant_dias} dias, {quant_horas} horas,{quant_minutos} minutos é igual a {total_segundos} segundos")


def aumento_salario():
    salario = float(input("Qual o valor do salario?\n"))
    aumento = float(input("Qual o valor percentual do aumento?\n"))
    aumento_salario = salario + (salario / aumento)
    print(f"O novo salario com aumento de R${salario / aumento} é de R${aumento_salario}")


def desconto_mercadoria():
    preco = float(input("Digite o preço da mercadoria:\n"))
    desconto = int(input("Digite a porcentagem de desconto:\n"))
    mercadoria_desconto = preco - (preco / desconto)
    print(f"O novo preço do produto é de R${mercadoria_desconto:4.2f} com o desconto de R${(preco / desconto):3.1f}")


def tempo_viagem():
    distancia_viagem = float(input("Digite a distancia a ser percorrida em kilometros:\n"))
    velocidade_media = int(input("Digite a velocidade média durante o trajeto:\n"))
    viagem_tempo = distancia_viagem / velocidade_media
    print(f"Você vai demorar {viagem_tempo:3.1f} horas para chegar no seu destino")


def conversor_temperatura():
    celsius = float(input("Digite a temperatura em Celsius:\n"))
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f"A temperatura em fahrenheit é de {fahrenheit}")


def aluguel_carro():
    dias_alugados = int(input("Por quantos dias o carro foi alugado?\n"))
    km_andados = float(input("Qual a distancia percorrida pelo carro nesse periodo?\n"))
    preco_aluguel = (dias_alugados * 60) + (km_andados * 0.15)
    print(f"O valor total do aluguel é de R${preco_aluguel}")


def tempo_de_vida():
    cigarros = int(input("Quantos cigarros você fuma por dia? "))
    tempo = int(input("Você fuma a quantos anos? "))
    cigarros_totais = cigarros * (tempo * 365)
    tempo_perdido = ((cigarros_totais * 10) / 6) / 24
    print(f"Você perdeu {tempo_perdido} dias de vida")


while not pergunta:
    print('''
    ####################################################################################################################
    Que exercicio você quer ver?
    1) Soma de numeros inteiros
    2) Conversor de metros em milimetros
    3) Conversor de tempo em segundos
    4) Calculadora de aumento de salario
    5) Calculadora de desconto em mercadoria
    6) Calculadora de tempo de viagem
    7) Conversor de graus Celsius em Fahrenheit
    8) Calculadora de aluguel de carro
    9) Calculadora de perda de dias de vida por cigarros
    0) Fechar programa
    
    IMPORTANTE: Todos os exercicios foram retirados do livro Introdução a Programação com Python, pagina 72.
    ####################################################################################################################
    ''')
    pergunta = int(input("Digite o numero do exercicio que deseja ver: "))

    if pergunta == 1:
        soma_numeros()
    elif pergunta == 2:
        conversor_metros()
    elif pergunta == 3:
        conversor_segundos()
    elif pergunta == 4:
        aumento_salario()
    elif pergunta == 5:
        desconto_mercadoria()
    elif pergunta == 6:
        tempo_viagem()
    elif pergunta == 7:
        conversor_temperatura()
    elif pergunta == 8:
        aluguel_carro()
    elif pergunta == 9:
        tempo_de_vida()
    elif pergunta == 0:
        exit(0)
    else:
        print("Opção invalida, digite de novo")
    pergunta = False
