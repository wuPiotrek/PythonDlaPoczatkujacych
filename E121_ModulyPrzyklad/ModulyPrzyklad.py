#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

import random

min = 1
max = 6

dice = random.randint(min, max)
print(dice)

if dice == 1:
    print('   ')
    print(' o ')
    print('   ')

elif dice == 2:
    print('  o')
    print()
    print('o  ')

elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')

elif dice == 4:
    print('o o')
    print()
    print('o o')

elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')

else:
    print('o o')
    print('o o')
    print('o o')

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

dices = []

for throw in range(5):
    dice = random.randint(min, max)
    dices.append(dice)

dices.sort()
print(dices)
    
#################################################
