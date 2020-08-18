import random
import sys

global GameBoard

# Fonction affichant le plateau de jeu
def printboard(board):
    print("\n" + board['up_l'] + '|' + board['up_m'] + '|' + board['up_r'] + '\n' + '--+--+--' + '\n' + board['mid_l'] + '|' + board['mid_m'] + '|' + board['mid_r'] + '\n' + '--+--+--' + '\n' + board['low_l'] + '|' + board['low_m'] + '|' + board['low_r'])

# Fonction permettant au joueur de choisir son camp
# côté joueur = a
# côté IA = b
def playerside():

    global a, b, GameBoard

    # Charger / Recharger le plateau de jeu
    GameBoard = {'up_l': '[]', 'up_m': '[]', 'up_r': '[]', 'mid_l': '[]', 'mid_m': '[]','mid_r': '[]', 'low_l': '[]', 'low_m': '[]', 'low_r': '[]'}

    a = input("Do you want to play with O or X ? ")

    if a == 'O':
        b = '[X]'

    elif a == 'o':
        b = '[X]'

    elif a == 'X':
        b = '[O]'

    elif a == 'x':
        b = '[O]'

    else:
        print("I didn't understand your request. Please try again.")
        playerside()

# Fonction affichant les déplacements possibles
def printpos():
    print("\nPositions : up_l | up_m | up_r | mid_l | mid_m | mid_r | low_l | low_m | low_r |")
    print("Enter 'quit' to exit program.")

# Fonction representant le tour du joueur
def yourturn():
    pos = input("It's your turn, enter a position :")

    if pos == 'up_l' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'

    elif pos == 'up_m' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'
    
    elif pos == 'up_r' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'

    elif pos == 'mid_l' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'

    elif pos == 'mid_m' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'
    
    elif pos == 'mid_r' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'

    elif pos == 'low_l' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'
    
    elif pos == 'low_m' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'
    
    elif pos == 'low_r' and GameBoard[pos] == '[]':
        GameBoard[pos] = f'[{a}]'

    elif pos == 'quit':
        sys.exit(0)

    else:
        print("Wrong move. Please try again.")
        yourturn()

    printboard(GameBoard)

# Fonction representant le tour de l'IA
def histurn():
    moves = ["up_l", "up_m", "up_r", "mid_l", "mid_m", "mid_r", "low_l", "low_m", "low_r"]
    hismove = random.choice(moves)

    if hismove == 'up_l' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b

    elif hismove == 'up_m' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b
    
    elif hismove == 'up_r' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b

    elif hismove == 'mid_l' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b

    elif hismove == 'mid_m' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b
    
    elif hismove == 'mid_r' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b

    elif hismove == 'low_l' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b
    
    elif hismove == 'low_m' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b
    
    elif hismove == 'low_r' and GameBoard[hismove] == '[]':
        GameBoard[hismove] = b

    else:
        histurn()

    printboard(GameBoard)


# Fonction demandant au joueur si il souhaite rejouer
def playagain():
    global i
    playagain = input('Play again (y/n) ? ')
    if playagain == 'y':
        game()
    elif playagain == 'n':
        sys.exit(0)
    else:
        print("Wrong answer, try again.")


# Fonction representant le jeu à tour de rôle
def game():
    # Fonction permettant au joueur de choisir son camp
    playerside()

    # Fonction affichant le plateau
    printboard(GameBoard)

    # Boucle du jeu
    i = True
    while i == True:

        # Fonction representant le tour du joueur
        printpos()
        yourturn()
        # Fonction representant le tour de l'IA
        histurn()

        # Conditions si une des lignes est remplie par le joueur
        if GameBoard['up_l'] == f'[{a}]' and GameBoard['up_m'] == f'[{a}]' and GameBoard['up_r'] == f'[{a}]':
            print("This game is over. You won !")
            playagain()

        if GameBoard['mid_l'] == f'[{a}]' and GameBoard['mid_m'] == f'[{a}]' and GameBoard['mid_r'] == f'[{a}]':
            print("This game is over. You won !")
            playagain()

        if GameBoard['low_l'] == f'[{a}]' and GameBoard['low_m'] == f'[{a}]' and GameBoard['low_r'] == f'[{a}]':
            print("This game is over. You won !")
            playagain()

        # Conditions si une des colonnes est remplie par le joueur
        if GameBoard['up_l'] == f'[{a}]' and GameBoard['mid_l'] == f'[{a}]' and GameBoard['low_l'] == f'[{a}]':
            print("This game is over. You won !")
            playagain()

        if GameBoard['up_m'] == f'[{a}]' and GameBoard['mid_m'] == f'[{a}]' and GameBoard['low_m'] == f'[{a}]':
            print("This game is over. You won !")
            playagain()

        if GameBoard['up_r'] == f'[{a}]' and GameBoard['mid_r'] == f'[{a}]' and GameBoard['low_r'] == f'[{a}]':
            print("This game is over. You won !")
            playagain()

            # Conditions si une des diagonales est remplie par le joueur
        if GameBoard['up_l'] == f'[{a}]' and GameBoard['mid_m'] == f'[{a}]' and GameBoard['low_r'] == f'[{a}]':
            print("This game is over. You won !")
            playagain()

        if GameBoard['up_r'] == f'[{a}]' and GameBoard['mid_m'] == f'[{a}]' and GameBoard['low_l'] == f'[{a}]':
            print("This game is over. You won !")
            playagain()


        # Conditions si une des lignes est remplie par l'IA
        if GameBoard['up_l'] == b and GameBoard['up_m'] == b and GameBoard['up_r'] == b:
            print("This game is over. You lose.")
            playagain()

        if GameBoard['mid_l'] == b and GameBoard['mid_m'] == b and GameBoard['mid_r'] == b:
            print("This game is over. You lose.")
            playagain()

        if GameBoard['low_l'] == b and GameBoard['low_m'] == b and GameBoard['low_r'] == b:
            print("This game is over. You lose.")
            playagain()

        # Conditions si une des colonnes est remplie par l'IA
        if GameBoard['up_l'] == b and GameBoard['mid_l'] == b and GameBoard['low_l'] == b:
            print("This game is over. You lose.")
            playagain()

        if GameBoard['up_m'] == b and GameBoard['mid_m'] == b and GameBoard['low_m'] == b:
            print("This game is over. You lose.")
            playagain()

        if GameBoard['up_r'] == b and GameBoard['mid_r'] == b and GameBoard['low_r'] == b:
            print("This game is over. You lose.")
            playagain()

        # Conditions si une des diagonales est remplie par l'IA
        if GameBoard['up_l'] == b and GameBoard['mid_m'] == b and GameBoard['low_r'] == b:
            print("This game is over. You lose.")
            playagain()

        if GameBoard['up_r'] == b and GameBoard['mid_m'] == b and GameBoard['low_l'] == b:
            print("This game is over. You lose.")
            playagain()

    else:
        i = False
        sys.exit(0)

# Plateau de jeu en global pour être utilisé par des fonctions
GameBoard = {'up_l': '[X]', 'up_m': '[X]', 'up_r': '[X]', 'mid_l': '[]', 'mid_m': '[]','mid_r': '[]', 'low_l': '[]', 'low_m': '[]', 'low_r': '[]'}

game()