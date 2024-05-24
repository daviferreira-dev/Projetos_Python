def adicao(a, b):   #função para adição
    return a + b

def subtracao(a, b):    #função para subtração
    return a - b

def multiplicacao(a, b):    #função para multiplicação
    return a * b

def divisao(a, b):  #função para divisão
    if b == 0:
        return "Erro: Todo número dividido por 0 é 0!"
    else:
        return a / b

print("Calculadora Simples")
print("Escolha a operação:")
print("1 para Adição")
print("2 para Subtração")
print("3 para Multiplicação")
print("4 para Divisão")

opcao = int(input("Digite sua escolha (1/2/3/4): "))

# verifica qual opção foi escolhida
if opcao in (1, 2, 3, 4):
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if (opcao == 1):
        print("Resultado da adição:", adicao(numero1, numero2))
    elif (opcao == 2):
        print("Resultado da subtração:", subtracao(numero1, numero2))
    elif (opcao == 3):
        print("Resultado da multiplicação:", multiplicacao(numero1, numero2))
    elif (opcao == 4):
        print("Resultado da divisão:", divisao(numero1,numero2))
else:
    print("Opção inválida. Por favor, reinicie o programa e escolha uma opção válida (1/2/3/4).")