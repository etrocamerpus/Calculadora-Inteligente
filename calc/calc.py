print("Calculadora Inteligente")
sair = False

while sair == False:

    numero1 = input("Digite o primeiro numero:")
    numero1 = int(numero1)
    operador = input("Agora o sinal:")
    numero2 = input("Digite o segundo numero:")
    numero2 = int(numero2)

    # + soma
    if operador == "+":
        operacao = numero1 + numero2

    # - subtração
    if operador == "-":
        operacao = numero1 - numero2

    # / divisão
    if operador == "/":
        operacao = numero1 / numero2

    # * multiplicação
    if operador == "*":
        operacao = numero1 * numero2

    print("Resultado:")
    print(operacao)

    repetir = input("Quer executar outro calculo? s/n:")
    if repetir == "n":
        sair = True