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

print("Greetings and Welcome to High Roller.")
time.sleep(1)
name_one = input("Player One, please enter your name: ")
time.sleep(1)
name_two = input("Player Two, please enter your name: ")
time.sleep(1)
print("Prepare to duel, {} and {}.".format(name_one, name_two))
go = input("Press Enter to roll, {}".format(name_one))

roll_one = random.randrange(1,6)

if roll_one == 1:
    one()
elif roll_one == 2:
    two()
elif roll_one == 3:
    three()
elif roll_one == 4:
    four()
elif roll_one == 5:
    five()
elif roll_one == 6:
    six()
else:
    print("Whoa, what did you roll?")
    

class Player_One(self):

