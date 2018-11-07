#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

number = 1
previus_number = 0
 
while number<50:
    print(number + previus_number)
    previus_number=number
    number += 1

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

text = ''
number = 10
condition = True
 
while condition:
 
    text+='x'
    print(text)
    
    if len(text)>= number:
        condition=False

#################################################
