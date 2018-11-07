#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

MIN_LIKES = 500
MIN_SHARES = 100
# Warunki wejściowe:
num_likes = 150
num_shares = 150    
# -
if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('Warunki spełnione, ceny zostaną obniżone o 10%')
else:
    print('Zbyt mała aktywność, ceny nie zostaną obniżone')
        
#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

# Warunki wejściowe:
isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False
# -
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Dostajesz kupon na burgera')
else:
    print('Zachęcamy do dalszych zakupów')
       
#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

# Warunki wejściowe:
diskSize = 140
diskSizeUsed = 133
fileSize = 10
# -
if (diskSize - diskSizeUsed) >= fileSize:
    print("File can be downloaded")
else:
    print("No enought disc space!")

#################################################
