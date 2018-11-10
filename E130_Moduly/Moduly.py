#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

import math

if len(inputdata) == len(factortable):

    i = 0
    while i < len(inputdata):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print('minvalue', minvalue)
        print('maxvalue', maxvalue)
        print()
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, inputdata[i], maxinteger)
        print('---')
        i += 1
            
else:
    
    print('inputdata and factortable need to have equal number of elements')

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

import random

i = 0
while i < len(inputdata):
    x = random.random()
    print(x)
    minvalue = inputdata[i] - x * inputdata[i]
    maxvalue = inputdata[i] + x * inputdata[i]
    print('minvalue', minvalue)
    print('maxvalue', maxvalue)
    print()
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger, inputdata[i], maxinteger)
    print('---')
    i += 1

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

from datetime import datetime

print(datetime.today())
print(datetime.today().strftime('%Y-%m-%d'))

#################################################
