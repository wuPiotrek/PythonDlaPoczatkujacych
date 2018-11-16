##The application is indended to read file created in previous excercise, show
##saved adresses in compiler and show information does the adress is from poland domain

import os

currentDir = os.getcwd()
fileName = input('Enter a file name: ')
filePath = os.path.join(currentDir, fileName + '.txt')
print()

while not os.path.isfile(filePath):

    print('!! Typed file do not exists !!')
    fileName = input('Enter a file name: ')
    filePath = os.path.join(currentDir, fileName)

webadresses = []

with open(filePath, 'r') as file:

    for line in file:

        line = line.replace('\n', '')
        webadresses.append(line)

        
for adress in webadresses:

    if adress.endswith('.pl'):

        print('{:20s} is a polish web page.'.format(adress))

    else:

        print('{:20s} is not a polish web page!!!'.format(adress))
