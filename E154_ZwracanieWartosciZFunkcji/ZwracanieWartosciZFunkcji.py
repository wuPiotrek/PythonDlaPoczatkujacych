#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

def PrintAnimal(animal = None):
   
    if animal == 'cat':
        txt = r'''
        |\---/|
        | o_o |
         \_^_/'''
        print(txt)

    elif animal == 'bear':
        txt = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
        print(txt)

    elif animal == 'bat':
        txt = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/'''
        print(txt)

    elif type(animal) == str:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % (animal))
        return False
        
    else:
        print('Correct values for the parameter are: cat, bear, bat')
        return False

    return True           

#Function executions:

if PrintAnimal('cat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')

print()

if PrintAnimal('bear'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
    
print()

if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')

print()

if PrintAnimal('spider'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
    
print()

if PrintAnimal():
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
    



#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

from datetime import date
from datetime import timedelta

def DaysTillEndYear(year    = date.today().year,\
                    month   = date.today().month,\
                    day     = date.today().day):    
   
    day = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - day

    return delta.days

dateToCalc = DaysTillEndYear(2018, 11, 12)
print('Date: 2018-11-12 days to end of year:', dateToCalc)
dateToCalc = DaysTillEndYear(2018, 11, 10)
print('Date: 2018-11-10 days to end of year:', dateToCalc)
dateToCalc = DaysTillEndYear(2017, 11, 11)
print('Date: 2017-11-11 days to end of year:', dateToCalc)
dateToCalc = DaysTillEndYear(2018, 10, 11)
print('Date: 2018-10-11 days to end of year:', dateToCalc)
dateToCalc = DaysTillEndYear(2018, 1, 1)
print('Date: 2018-01-01 days to end of year:', dateToCalc)
dateToCalc = DaysTillEndYear(day = 1, month = 2, year = 2005)
print('Date: 2005-02-01 days to end of year:', dateToCalc)
dateToCalc = DaysTillEndYear()
print('Date: Empty = TODAY days to end of year:', dateToCalc)

#################################################
