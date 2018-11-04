print('1:')
yearOfBirth = 1993
shoeSize = 44
print(((shoeSize * 5 + 50) * 20 + 1018) - yearOfBirth)

print('\n2:')
theNumber = 51
print((theNumber * 2 + 10) / 2 - theNumber)

print('\n3:')
print(2 + 2 * 2)
print(7 + 7 / 7 + 7 * 7 - 7)

print('\n4:')
attendance = 0.85
gradesAverage = 3.5
semesterWork = False
ifComplete = (attendance > 0.8 and gradesAverage >= 3.0) or semesterWork
print('Frekwencja        :', attendance)
print('Średnia ocen      :', gradesAverage)
print('Praca semestralna :', semesterWork)
print("Czy zaliczy?      :", ifComplete)

print('\n5:')
attendance = 0.85
gradesAverage = 3.5
semesterWork = False
ifComplete = attendance > 0.8 and gradesAverage >= 3.0 and semesterWork
print('Frekwencja        :', attendance)
print('Średnia ocen      :', gradesAverage)
print('Praca semestralna :', semesterWork)
print("Czy zaliczy?      :", ifComplete)

print('\n6:')
print('KRYTERIUM PIERWSZE')
attendance = 0.40
gradesAverage = 2.5
semesterWork = True
ifComplete = (attendance > 0.8 and gradesAverage >= 3.0) or semesterWork
print('Frekwencja        :', attendance)
print('Średnia ocen      :', gradesAverage)
print('Praca semestralna :', semesterWork)
print("Czy zaliczy?      :", ifComplete)

print('KRYTERIUM DRUGIE')
attendance = 0.40
gradesAverage = 2.5
semesterWork = True
ifComplete = attendance > 0.8 and gradesAverage >= 3.0 and semesterWork
print('Frekwencja        :', attendance)
print('Średnia ocen      :', gradesAverage)
print('Praca semestralna :', semesterWork)
print("Czy zaliczy?      :", ifComplete)

