#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

import math

# Function counts elements of geometric progression

def GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):

    # a1        - first element
    # factor    - geometric factor 
    # index     - index of element to count 

    value = a1 * pow(factor, index - 1)
    return value

print('2^64 is:')
print(GiveGeomSeqElement(1, 2, 64))

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

a1 = 3
factor = 2
maxindex = 10

for i in range(1, maxindex + 1):

    element = GiveGeomSeqElement(a1, factor, i)
    print('Term {:2d} = {:d}'.format(i, element))
    
#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

# Function counts value of geometrical progression factor from firs and second element

def GiveFactorForGeomSeq(term, nexterm):
    
    # term      - firs term's value
    # next term - second term's value

    factor = nexterm / term
    return factor

argument1 = 12
argument2 = 24

print('For terms: {:d} and {:d} \nthe FACTOR is: {:d}'.format(argument1, argument2, factor))


#################################################
exNumber = 4
print("-" * 5, exNumber, "-" * 30)
# Code:

