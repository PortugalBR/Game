#main page of the games!
def mainMenu():
    print('*********************************')
    print('******* Choose a language *******')
    print('*********************************')

    print('-=-=-=-=-=-=-=-=-')
    print("1. English")
    print('-=-=-=-=-=-=-=-=-')
    print("2. Portuguese")
    print('-=-=-=-=-=-=-=-=-')
    print("3. Spanish")
    print('-=-=-=-=-=-=-=-=-')
    print("4. German")
    print('-=-=-=-=-=-=-=-=-')
    print("5. Quit")
    print('-=-=-=-=-=-=-=-=-')

    while True:
        try:
            selection = int(input("Enter a choice: "))
            if selection == 1:
                def chose_game():

                    import TheHangman
                    import guessgame

                    print('*****************************')
                    print('******* Chose a game !*******')
                    print('*****************************')

                    print("(1) The Hangman (2) Guess game")

                    jogo = int(input("Wich game ? "))

                    if (jogo == 1):
                        print("Playing The Hangman")
                        TheHangman.jogar()
                    elif (jogo == 2):
                        print("Playing Guess game")
                        guessgame.jogar()

                if (__name__ == '__main__'):
                    chose_game()



            elif selection == 2:

                import forca
                import jogodeadivinhacaomelhorado

                def escolhe_jogo():
                    print('**********************************')
                    print('******* Escolha o seu jogo!*******')
                    print('**********************************')
                    print('                                  ')
                    print("(1) Forca (2) Adivinhação")

                    jogo = int(input("Qual jogo? "))

                    if (jogo == 1):
                        print("Jogando forca")
                        forca.jogar()

                    elif (jogo == 2):
                        print("Jogando adivinhação")
                        jogodeadivinhacaomelhorado.jogar()

                if (__name__ == '__main__'):
                    escolhe_jogo()

            elif selection == 3:

                import El_ahorcado
                import advinanzas

                def elige_juego():
                    print('*****************************')
                    print('*******Elige un juego *******')
                    print('*****************************')
                    print('                                  ')
                    print("(1) El ahorcado (2) Advinanzas")

                    jogo = int(input("Qual jogo? "))

                    if (jogo == 1):
                        print("Jugando al ahorcado")
                        El_ahorcado.jogar()

                    elif (jogo == 2):
                        print("Jugando a advinar ")
                        advinanzas.jogar()

                if (__name__ == '__main__'):
                    elige_juego()



            elif selection == 4:
                def wahle_spiel():

                    import Henker_Spiel
                    import Divination

                    print('**************************************')
                    print('****** Wählen Sie eine Sprache *******')
                    print('**************************************')

                    print("(1) Der Henker (2) Ratespiel ")

                    jogo = int(input(" Welches Spiel? "))

                    if (jogo == 1):
                        print("Playing der Henker")
                        Henker_Spiel.jogar()
                    elif (jogo == 2):
                        print("Playing Ratespiel")
                        Divination.jogar()

                if (__name__ == '__main__'):
                    wahle_spiel()


                break
            elif selection == 5:
                break
            else:
                print("Invalid choice. Enter 1-5.")
        except ValueError:
            print("Invalid choice! Choose 1-5!!")






mainMenu()


