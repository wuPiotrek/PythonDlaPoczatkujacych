#################################################
exNumber = 1, 2, 3
print("-" * 5, exNumber, "-" * 30)
# Code:

import math

degree = 360

print(degree, 'stopni to', round((degree * math.pi/180), 2), 'radianów')

#################################################
exNumber = 4
print("-" * 5, exNumber, "-" * 30)
# Code:

import math

degree = 45

print(degree, 'stopni to', round((degree * math.pi/180), 2), 'radianów')

#################################################
exNumber = 5
print("-" * 5, exNumber, "-" * 30)
# Code:

print(math.radians(45))
print(math.radians(360))

#################################################
exNumber = 6, 7
print("-" * 5, exNumber, "-" * 30)
# Code:

from math import pi

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38

small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

def surface(radius):
    result = pi * (radius ** 2) / (100 ** 2)
    return result
print('Pole powierzchni pizzy:')
print('%8s : %.2f m^2' % ('small', surface(small_pizza_r)))
print('%8s : %.2f m^2' % ('big', surface(big_pizza_r)))
print('%8s : %.2f m^2' % ('family', surface(family_pizza_r)))

#################################################
exNumber = 8
print("-" * 5, exNumber, "-" * 30)
# Code:

def meterPrice(radius, price):
    result = price / surface(radius)
    return result

print('Cena za metr kwadratowy pizzy:')
print('%8s : %.2f zł/m^2' % ('small', meterPrice(small_pizza_r, small_pizza_price)))
print('%8s : %.2f zł/m^2' % ('big', meterPrice(big_pizza_r, big_pizza_price)))
print('%8s : %.2f zł/m^2' % ('family', meterPrice(family_pizza_r, family_pizza_price)))

#################################################

