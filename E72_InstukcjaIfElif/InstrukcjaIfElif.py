#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

MIN_LIKES = 500
MIN_SHARES = 100
# Warunki wejściowe:
num_likes = 550
num_shares = 505    
# -
print('*Wersja pierwsza:')
if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('Warunki spełnione, ceny zostaną obniżone o 10%')
else:
    if num_likes < MIN_LIKES:
        print('Zbyt mało polubień')
    else:
        print('Zbyt mało udostępnień')

print('*Wersja druga:')
if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('Warunki spełnione, ceny zostaną obniżone o 10%')
elif num_likes < MIN_LIKES:
    print('Zbyt mało polubień')
else:
    print('Zbyt mało udostępnień')
    
#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

# Warunki wejściowe:
isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False
# -
print('*Wersja pierwsza:')
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Dostajesz kupon na burgera')
else:
    if isWeekend:
        print('Promocja dotyczy tylko dni poza weekendem')
    else:
        print('Nie zamówiono pizzy')

print('*Wersja druga:')
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Dostajesz kupon na burgera')
elif isWeekend:
    print('Promocja dotyczy tylko dni poza weekendem')
else:
    print('Należy zamówić pizzę lub duży napój')

#################################################
