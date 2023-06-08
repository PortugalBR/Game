import random
from time import sleep

def jogar():
    print("**********************************")
    print("*** Willkommen beim Ratespiel! ***")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print(" Was ist der Schwierigkeitsgrad? ")
    print("(1) Leicht (2) Mittel (3) Schwer")

    nivel = int(input("Stellen Sie den Pegel ein: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Versuch {} von {}".format(rodada, total_de_tentativas))

        chute_str = input("Geben Sie eine Zahl zwischen 1 und 100 ein: ")
        print("Du hast getippt ", chute_str)
        chute = int(chute_str)
        sleep(1)

        if (chute < 1 or chute > 100):
            print("Sie müssen eine Zahl zwischen 1 und 100 eingeben!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Du hast es richtig gemacht und {} Punkte erzielt!".format(pontos))
            sleep(1)
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Ihre Vermutung war größer als die Geheimzahl")
                if (rodada == total_de_tentativas):
                    print("Die Geheimnummer war {}. Du machtest {}".format(
                        numero_secreto, pontos))
                    print('*********************************')
            elif (menor):
                print("Du hast verpasst! Ihre Schätzung war niedriger als die Geheimzahl.")
                if (rodada == total_de_tentativas):
                    print("Die Geheimnummer war {}. Du hast {} Punkte gemacht".format(
                        numero_secreto, pontos))
                    print('*********************************')

    print("Endspiel!")
    sleep(1)

    print('*******************************')
    print('****** Chose a language *******')
    print('*******************************')

    print("1. English")
    print("2. Português")
    print("3. Spanish")
    print("4. German")
    print("5. Quit")


if (__name__=="__main__"):
    jogar()