#################################################
exNumber = 1, 2
print("-" * 5, exNumber, "-" * 30)
# Code:

import time

print(time.time())

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

print(time.localtime(time.time()))

#################################################
exNumber = 4, 5
print("-" * 5, exNumber, "-" * 30)
# Code:

import calendar

print('Miesiąc urodzenia: Styczeń')
print(calendar.month(1993, 1))

#################################################
exNumber = 6, 7
print("-" * 5, exNumber, "-" * 30)
# Code:

calendar.setfirstweekday(6)

print('Miesiąc urodzenia: Styczeń')
print(calendar.month(1993, 1))

#################################################
exNumber = 8
print("-" * 5, exNumber, "-" * 30)
# Code:

print('Czy 2000 rok był rokiem przestępnym?', calendar.isleap(2000))

#################################################
exNumber = 9
print("-" * 5, exNumber, "-" * 30)
# Code:

print(calendar.calendar(2019))

#################################################
