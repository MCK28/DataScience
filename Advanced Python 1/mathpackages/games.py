'''This module contains a couple games created by defining a function'''

# First game: rock-paper-scissors
import random
def rps():
    pc_choices = ['r', 'p', 's']
    while True:
        pc = pc_choices[random.randint(0, 2)]
        user = input('For rock:r, for paper:p, for scissors:s, and to exit the game, enter q').lower()
        if user == 'q':
            print('Exiting game...')
            break
        elif pc == user:
            print(f'PC: {pc}, User: {user}. It is a tie')
        elif (pc == 'r' and user == 's') or (pc == 's' and user == 'p') or (pc == 'p' and user == 'r'):
            print(f'PC: {pc}, User: {user}. PC Won!')
        elif (pc == 's' and user == 'r') or (pc == 'p' and user == 's') or (pc == 'r' and user == 'p'):
            print(f'PC: {pc}, User: {user}. You Won!')
        else:
            print('Please enter valid inputs as r, p, s and for quitting q.')