#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for color in colors:

    for figure in figures:

        aCard = figure.copy()
        aCardUpdate = {'Color':color}
        aCard.update(aCardUpdate)
        allCards.append(aCard)

for i in allCards:
    print(i)

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

import random

random.shuffle(allCards)

for i in allCards:
    print(i)

#################################################
exNumber = 3, 4
print("-" * 5, exNumber, "-" * 30)
# Code:

player1 = []
player2 = []
maxValue = len(allCards)

for i in range(maxValue):
    
    if i % 2 == 0:
        player1.append(allCards[i])

    else:
        player2.append(allCards[i])   

print("First player's cards:")

for i in player1:
    print(i)
    
print()

print("Second player's cards:")

for i in player2:
    print(i)

#################################################
exNumber = 5, 6, 7
print("-" * 5, exNumber, "-" * 30)
# Code:

while len(player1) > 0 and len(player2) > 0:
    
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        print('Draw')
        
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print('Player1 wins')
        
    elif card1["Power"] < card2["Power"]:
        player2.append(card1)
        player2.append(card2)
        print('Player2 wins')
        
    print('Number of Player1\'s cards:', '*' * len(player1) )
    print('Number of Player2\'s cards:', '*' * len(player2) )
    print()

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
    
else:
    print('PLAYER 2 WON!!!!')

