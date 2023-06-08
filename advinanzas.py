import random
from time import sleep

def jogar():
    print("********************************************")
    print("*** ¡Bienvenido al juego de adivinanzas! ***")
    print("********************************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("¿Cuál es el nivel de dificultad?")
    print("(1) Fácil (2) Medio (3) Difícil")

    nivel = int(input("Establecer el nivel:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Introduzca un número entre 1 y 100: ")
        print(" Escribiste ", chute_str)
        chute = int(chute_str)
        sleep(1)

        if (chute < 1 or chute > 100):
            print("¡Debes ingresar un número entre 1 y 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("¡Lo hiciste bien y obtuviste {} puntos!".format(pontos))
            sleep(1)
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Tu conjetura fue más grande que el número secreto")
                if (rodada == total_de_tentativas):
                    print("El número secreto era {}. Lo hiciste {}".format(
                        numero_secreto, pontos))
                    print('*********************************')
            elif (menor):
                print("¡Te lo perdiste! Su conjetura fue menor que el número secreto.")
                if (rodada == total_de_tentativas):
                    print("El número secreto era {}. Hiciste {} Puntos".format(
                        numero_secreto, pontos))
                    print('*********************************')

    print("Fin del juego!")
    sleep(1)

    print('******************************')
    print('****** Elige un idioma *******')
    print('*******************************')

    print("1. inglés")
    print("2. Português")
    print("3. Español")
    print("4. Alemán")
    print("5. Quit")


if (__name__=="__main__"):
    jogar()