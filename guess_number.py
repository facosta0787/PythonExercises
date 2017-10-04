# -*- coding: utf-8 -*-
import random

def run():
    found = False
    rand = random.randint(1,10)
    while not found:
        number = int(input('Input a nummber between {} and {} : '.format(1,10)))
        if number == rand:
            print('The number was found')
            found = True
        elif number > rand:
            print ('The number is smaller')
        else:
            print('The number is bigger')

if __name__ == '__main__':
    run()
