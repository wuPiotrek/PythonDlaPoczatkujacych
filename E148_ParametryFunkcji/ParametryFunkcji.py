#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

def PrintAnimal(animal):
   
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

    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % (animal))
        
    return

PrintAnimal('cat')
PrintAnimal('bear')
PrintAnimal('bat')
PrintAnimal('elephant')

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

def DaysTillEndYear(year, month, day):

    from datetime import date, timedelta

    day = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - day
    print(delta.days)

    return

DaysTillEndYear(2018, 11, 12)
DaysTillEndYear(2018, 11, 11)
DaysTillEndYear(2017, 11, 11)
DaysTillEndYear(2018, 10, 11)
DaysTillEndYear(2018, 1, 1)
DaysTillEndYear(day = 1, month = 2, year = 2005)

#################################################
