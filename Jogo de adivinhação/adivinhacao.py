import random

def mensagem_de_erro(msg):
    print("\n" * 50)
    print("-" * (len(msg) + 2))
    print("|" + msg + "|")
    print("-" * (len(msg) + 2))

def jogar():
    print("*******************************************")
    print("bem vindo ao jogo de adivinhação de numeros")
    print("*******************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    result = "s"

    while result.lower() == "s":
        print("qual o nivel de dificuldade?")
        print("1 - Facil")
        print("2 - Médio")
        print("3 - Dificil")

        nivel = int(input("Defina um nível: "))

        if (nivel == 1):
            total_de_tentativas = 20
        elif (nivel == 2):
            total_de_tentativas = 10
        else:
            total_de_tentativas = 3


        rodada = 1
        while rodada <= total_de_tentativas:
            try:
                print("Tentativa {} de {}".format(rodada, total_de_tentativas))
                chute_str = input("digite um numero entre 1 e 100: ")
                chute = int(chute_str)

                print("Você digitou ", chute)

                if (chute < 1 or chute > 100):
                    print("Você é bobo? perdeu uma chance atoa, digita um numero entre 1 e 100:")

                    continue

                acertou = chute == numero_secreto
                maior = chute > numero_secreto
                menor = chute < numero_secreto

                if chute == numero_secreto:
                    print("Parabéns! quer um biscoito? vc acertou total de pontos = {} pontos!".format(pontos))
                    break
                elif chute > numero_secreto:
                    mensagem_de_erro("O seu chute foi maior do que o número secreto!")
                else:
                    mensagem_de_erro("O seu chute foi menor do que o número secreto!")

                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos = pontos - pontos_perdidos

                rodada = rodada + 1

            except Exception as error:
                mensagem_de_erro("para de por valores incorretos, preciso de numeros inteiros ¬¬'")

        print("numero secreto era:" + str(numero_secreto))
        print("total de pontos:" + str(pontos))
        result = input("Gostaria de jogar novamente? (S/N)")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()


