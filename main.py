import random
import time


def one():
    print('''
    -----------
   |           |
   |           |
   |     o     |
   |           |
   |           |
    -----------
    ''')

def two():
    print('''
    -----------
   |           |
   |     o     |
   |           |
   |     o     |
   |           |
    -----------
    ''')

def three():
    print('''
    -----------
   |           |
   |     o     |
   |     o     |
   |     o     |
   |           |
    -----------
    ''')

def four():
    print('''
    -----------
   |           |
   |   o   o   |
   |           |
   |   o   o   |
   |           |
    -----------
    ''')

def five():
    print('''
    -----------
   |           |
   |   o   o   |
   |     o     |
   |   o   o   |
   |           |
    -----------
    ''')

def six():
    print('''
    -----------
   |           |
   |   o   o   |
   |   o   o   |
   |   o   o   |
   |           |
    -----------
    ''')


def roller(r):
    if r == 1:
        one()
    elif r == 2:
        two()
    elif r == 3:
        three()
    elif r == 4:
        four()
    elif r == 5:
        five()
    elif r == 6:
        six()
    else:
        print('Ya done broke it!')

def game():    
    input('{}, press Enter to roll.'.format(name_one))
    roll_one = random.randrange(1,7)
    roller(roll_one)
    time.sleep(1)
    input('{}, press Enter to roll'.format(name_two))
    roll_two = random.randrange(1,6)
    roller(roll_two)
    time.sleep(2)

    if roll_one > roll_two:
        print('{} Wins.'.format(name_one))
    elif roll_one < roll_two:
        print('{} Wins.'.format(name_two))
    else:
        print('Tie!')

    again = input('Play again? ')
    again.islower()
    if again in ('yes', 'ye', 'y', 'yeah', 'yep', 'ya', 'yea'):
        game()
    else:
        print('Thanks for playing. Buhbye.')

def main():
    global name_one
    global name_two
    print("Greetings and Welcome to High Roller.")
    time.sleep(1)
    name_one = input("Player One, please enter your name: ")
    time.sleep(1)
    name_two = input("Player Two, please enter your name: ")
    time.sleep(1)
    print("Prepare to duel, {} and {}.".format(name_one, name_two))
    time.sleep(1)
    game()

main()
