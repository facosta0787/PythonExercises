# -*- coding: utf-8 -*-
import random
import sys

IMAGE = [
'''
    +---+
    |   |
        |
        |
        |
        |
        =========''',
'''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''',
'''
    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''',
'''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''',
'''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''',
'''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''',
'''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''',
'''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        ========='''
]

WORDS = ['java','python','javascript','go','c','csharp','cobol','pascal','ruby','scala','visualbasic','php','perl']


def randomWorld():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def tableBoard(hiddenWord, tries):
    print(IMAGE[tries])
    print('')
    print(hiddenWord)
    print('* ---------------------------------------------- *')

def run():
    word = randomWorld()
    hiddenWord = ['-'] * len(word)
    tries = 0
    while True:
        tableBoard(hiddenWord,tries)
        currentLetter = str(input('Ingresa una letra: '))
        letterIndexes = []
        for i in range(len(word)):
            if word[i] == currentLetter:
                letterIndexes.append(i)
        if len(letterIndexes) == 0:
            tries += 1
            if tries == (len(IMAGE) - 1):
                tableBoard(hiddenWord,tries)
                print('')
                print('¡ Perdiste ! la palabra correcta era {}'.format(word))
                break # Detiene los loops
        else:
            for idx in letterIndexes:
                hiddenWord[idx] = currentLetter
        letterIndexes = []
        try:
            hiddenWord.index('-')
        except ValueError:
            print('')
            print('Felicidades! Ganaste. La palabra es {}'.format(word))
            break

    resp = str(input('Deseas volver a jugar? type (yes/no): '))
    if resp == 'y' or resp == 'yes' or resp == 'Y' or resp == 'Yes':
        run()
    else:
        sys.exit(0)




if __name__ == ('__main__'):
    print('B I E N V E N I D O S  A L  A H O R C A D I T O')
    run()
