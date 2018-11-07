#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

i = 8
result = 1

for x in range (1, i + 1):
    result *= x
print(('%2d' % (i)) + '! = ' + str(result))

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

i = 10
result = 1

for x in range (1, i + 1):
    result *= x
    print(('%2d' % (x)) + '! = ' + str(result))

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(('%10s' % (adj)), noun)

#################################################
