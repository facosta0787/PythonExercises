# -*- coding: utf-8 -*-
import random

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

WORDS = ['Java','Python','JavaScript','Go','C','Csharp','Cobol','Pascal','Ruby','Scala','VisualBasic','PHP','Perl']


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

if __name__ == ('__main__'):
    print('B I E N V E N I D O S  A  A H O R C A D I T O')
    run()
