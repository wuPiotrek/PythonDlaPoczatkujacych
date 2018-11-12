#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

import geom

print('2 ^ 64 is:')
print(geom.GiveGeomSeqElement(2, 2, 64))

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

a1 = 3
factor = 2
maxindex = 10

for i in range(1, maxindex + 1):

    element = geom.GiveGeomSeqElement(a1, factor, i)
    print('Term {:2d} = {:d}'.format(i, element))
    
#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

argument1 = 12
argument2 = 24

tmpFactor = geom.GiveFactorForGeomSeq(argument1, argument2)

print('For terms: {:d} and {:d} \nthe FACTOR is: {:.0f}'.format(argument1, argument2, tmpFactor))


#################################################
exNumber = 4
print("-" * 5, exNumber, "-" * 30)
# Code:

print('Sum of 4 elements in geometrical progression starts from 2 with factor 3 is:')
print(geom.GiveSumOfNElementsGeomSeq(2, 3, 4))

#################################################



