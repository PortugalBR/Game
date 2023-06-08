import random
from time import sleep

def jogar():
    print("**********************************")
    print("*** Welcome to the guess game! ***")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print(" What is the difficulty level? ")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Set the level: "))

    if (level == 1):
        total_de_tentativas = 20
    elif (level == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Enter a number between 1 and 100: ")
        print("You typed ", chute_str)
        chute = int(chute_str)
        sleep(1)

        if (chute < 1 or chute > 100):
            print("You must enter a number between 1 and 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("You got it right and scored {} points!".format(pontos))
            sleep(1)
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Your guess was bigger than the secret number")
                if (rodada == total_de_tentativas):
                    print("The secret number was {}. You did {}".format(
                        numero_secreto, pontos))
                    print('*********************************')
            elif (menor):
                print("You missed! Your guess was lower than the secret number.")
                if (rodada == total_de_tentativas):
                    print("The secret number was {}. You made {} Points".format(
                        numero_secreto, pontos))
                    print('*********************************')

    print("EndGame!")
    sleep(1)

    print('*******************************')
    print('****** Choose a language *******')
    print('*******************************')

    print("1. English")
    print("2. Portuguese")
    print("3. Spanish")
    print("4. German")
    print("5. Quit")


if (__name__=="__main__"):
    jogar()