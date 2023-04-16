import random

def jogo_adivinhacao():

    print("**********************************")
    print("Bem vindos ao jogo de adivinhação!")
    print("**********************************")

    #variaveis
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    #niveis
    print('Qual nível de dificuldade?')
    print(" 1 - Fácil  2 - Médio  3 - Difícil")

    nivel = int(input('Defina um nivel: '))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    #laço
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        #chute
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        #condiçoes
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        #certo e errado
        if acertou:
            print('Você acertou! Total de pontos = {}'.format(pontos))
            break
        else:
            if maior:
                print('Você errou! Seu chute foi maior que o número secreto.')
            elif menor:
                print('Você errou! Seu chute foi menor que o número secreto.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('Fim de jogo.')

