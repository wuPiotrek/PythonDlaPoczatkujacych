#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

number = 1
previusNumber = 0

while number <= 50:
    print(previusNumber, '+', number, '=', previusNumber + number)
    previusNumber = number
    number += 1

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

import random
my_number = random.randint(0,20)

guess = -1
print('Guess my number!')

while guess != my_number:
    guess = int(input())
    if guess == my_number:
        print('Congratulations')
        break
    elif guess > my_number:
        print('Sorry- my number is smaller than your guess, Try again!')
        print('My number was:', my_number)
        print('Guess my number!')
    else:
        print('Sorry- my number is greatger than your guess, Try again!')
        print('My number was:', my_number)
        print('Guess my number!')
    my_number = random.randint(0,20)
    guess = -1

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

import random
my_number = random.randint(0,20)
guess = -1
trials = 0


while guess != my_number:    
    trials += 1
    print('Guess my number!')
    print('Próba nr', trials)
    guess = int(input())
    if guess == my_number:
        print('Congratulations!! Odgadłeś za', trials, 'razem!!')
        break
    elif guess > my_number:
        print('Sorry- my number is smaller than your guess, Try again!')
        print('My number was:', my_number)        
        print()
    else:
        print('Sorry- my number is greatger than your guess, Try again!')
        print('My number was:', my_number)
        print()
    my_number = random.randint(0,20)
    guess = -1

#################################################
