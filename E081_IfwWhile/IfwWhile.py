#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0

while i < len(numbers) - 1:
    print(numbers[i], '\t', numbers[i + 1])
    if numbers[i] ** 2 == (numbers[i + 1]):
        print ('FOUND')
    i += 1

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

x = 0

while x < len(numbers) - 2:
    print(numbers[x], '\t', numbers[x + 1], '\t', numbers[x + 2])
    if numbers[x] ** 2 == (numbers[x + 1]) and numbers[x + 1] ** 2 == (numbers[x + 2]):
        print ('FOUND')
    x += 1

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

z = 0

while z < len(texts) - 1:
    print(texts[z], '\t', texts[z + 1])
    if len(texts[z]) == len(texts[z + 1]):
        print ('  FOUND')
    z += 1

#################################################
