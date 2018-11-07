#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for item in data:
    print(item.upper())

    
#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

for item in data:
    element = item.split(':')
    print(element[0].upper() + '\t' + element[1])

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

for item in data:
    elements = item.split(':')
    if elements[0] == 'Error':
        print(elements[1].upper())
    else:
        print(elements[1])

#################################################
