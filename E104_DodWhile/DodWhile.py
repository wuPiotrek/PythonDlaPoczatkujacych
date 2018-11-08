#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

initialCapital = 20000
percent = 0.03
maxTimeYears = 10

print('Wpłacony kapitał:', initialCapital, 'PLN\n')

i = 1
current = initialCapital

while i <= maxTimeYears:
    current = round(current, 2) * (1 + percent)
    print('Stan konta po %2d roku: %.2f PLN' % (i, current))
    i += 1

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

number = int(20730906)
tmpNumber = number
result = 0

while tmpNumber > 0:
    tmp = tmpNumber % 10    
    result += tmp
    tmpNumber = tmpNumber // 10
else:
    print('Suma cyfr dla liczby', number, 'to:', result)

###############################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

txt = '''\
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.\
'''

listOfWords = txt.replace('\n', ' ').split(' ')

i = 0

#Długość wyrazu wyrazu
wordLength = 6

longWords = 0

longWordsList = []

while i < len(listOfWords):
    
    if len(listOfWords[i]) > wordLength:
        longWords += 1
        longWordsList.append(listOfWords[i])
        
    i += 1

print('Liczba słów dłuższych od 6:', longWords)
print('\nSłowa dłuższe od 6:\n', longWordsList)

###############################################

   
