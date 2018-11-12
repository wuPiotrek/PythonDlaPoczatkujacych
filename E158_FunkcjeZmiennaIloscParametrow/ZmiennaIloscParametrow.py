#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

def PrintAnimal(*animal):
    
    for element in animal:
   
        if element == 'cat':
            
            txt = r'''
            |\---/|
            | o_o |
             \_^_/'''
            print(txt)

        elif element == 'bear':
            
            txt = r'''
            /  \.-"""-./  \
            \    -   -    /
             |   o   o   |
             \  .-'"'-.  /
              '-\__Y__/-'
                 `---`'''
            print(txt)

        elif element == 'bat':
            
            txt = r'''
               /\                 /\
              / \'._   (\_/)   _.'/ \
             /_.''._'--('.')--'_.''._\
             | \_ / `;=/ " \=;` \ _/ |
              \/ `\__|`\___/`|__/`  \/
                      \(/|\)/'''
            print(txt)

        elif type(element) == str:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % (element))
            
        else:
            print('Correct values for the parameter are: cat, bear, bat')

    return         
#1
print('1' * 50)
PrintAnimal('cat')

#2
print('2' * 50)
PrintAnimal('bat', 'cat')

#3
print('3' * 50)
PrintAnimal('cat', 'bear', 'bat')

#4
print('4' * 50)
PrintAnimal('cat', 'bear', 'bat', 'elephant')

#5
print('5' * 50)
PrintAnimal('cat', 'bear', 'bat', 5)


#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

from datetime import date
from datetime import timedelta

def DaysTillEndYear(*dates):

    for currentDate in dates:
        
        date_end_year = date(currentDate.year, 12, 31)
        delta = date_end_year - currentDate
        print('Dla', currentDate, 'zostało', delta.days, 'dni do sylwestra')

    return

DaysTillEndYear(date(2018, 11, 12))
print(50 * '*')
DaysTillEndYear(date(2018, 11, 12), date(2017, 10, 12))
print(50 * '*')
DaysTillEndYear(date(2018, 11, 12), date(2017, 10, 12), date.today())

#################################################
