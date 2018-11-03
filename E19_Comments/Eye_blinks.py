# ilosc mrugnięć okiem na minutę

blinksPerMinute = 20

#ilość minut na godzinę i ilość godzin w dobie

minInHour = 60
hoursInDay = 24
daysInYear = 365

#ilość lat

years = 50

#ilość mrugnięć w ciągu x lat

blinksPerXYears = blinksPerMinute * minInHour * hoursInDay * daysInYear * years

print("W ciągu " + str(years) + " lat mrugniemy: " + str(blinksPerXYears) + " razy.")

##########################################

#definitionOfVariables
print()
daysOfWorkPerMonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
#result
print((daysOfWorkPerMonth * monthsInYear - vacation)*yearsOfWOrk)
