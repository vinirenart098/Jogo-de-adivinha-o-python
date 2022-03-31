import forca
import adivinhacao

def escolhe_jogo():

    print("******************")
    print("BEM VINDO AO MENU")
    print("*******************")

    print("Digite 1 para jogo da forca ou digite 2 para jogo de adivinhação de números")

    jogo = int(input("Qual jogo você quer?"))

    if (jogo == 1):
        print("executando jogo da forca")
        forca.jogar()
    elif (jogo == 2):
        print("executando jogo de adivinhação de números")
        adivinhacao.jogar()

if (__name__ == "__main__"):
        escolhe_jogo()

