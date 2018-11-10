#################################################
exNumber = 1, 2
print("-" * 5, exNumber, "-" * 30)
# Code:

import random

i = random.randrange(1, 100)

print(i)

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

number1 = random.randrange(1, 100)

counter = 1
number2 = random.randrange(1, 100)

print('Wylosowana liczba glówna to:', number1)
print()

while number2 != number1:
    number2 = random.randrange(1, 100)
    print('Próba %3d: Wylosowana liczba to: %2s' % (counter, number2))
    counter += 1
    
else:
    print()
    print('Wylosowano wartość odpowiadającą liczbie głównej po %d próbach' % (counter))

      
#################################################
exNumber = 4
print("-" * 5, exNumber, "-" * 30)
# Code:

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
groupNumber = 0
i = 0

for i in range(len(countries)):
    if i % 4 == 0:
        print('---- Grupa', i, '----')
    print(countries[i])

#################################################
