#################################################
exNumber = 1, 2, 3, 4
print("-" * 5, exNumber, "-" * 30)
# Code:

colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

for color in colors:

    for figure in figures:

        allCards.append((color + " " + figure))

print(allCards)

#################################################
exNumber = 5, 6
print("-" * 5, exNumber, "-" * 30)
# Code:

import random

random.shuffle(allCards)

print(allCards)

#################################################
exNumber = 7, 8
print("-" * 5, exNumber, "-" * 30)
# Code:

player1 = []
player2 = []

# First method:

maxValue = len(allCards)

for i in range(maxValue):
    
    if i % 2 == 0:
        player1.append(allCards[i])

    else:
        player2.append(allCards[i])   

print("First player's cards:\n", player1)
print()
print("Second player's cards:\n", player2)

#################################################
exNumber = 9
print("-" * 5, exNumber, "-" * 30)
# Code:

# Second method:

player1 = allCards[:12]
player2 = allCards[12:]

print("First player's cards:\n", player1)
print()
print("Second player's cards:\n", player2)

#################################################

