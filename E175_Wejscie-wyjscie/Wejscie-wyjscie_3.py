##The application is indended to read file created in previous excercise, show
##saved adresses in compiler and show information does the adress is from poland domain.
##The file is opened from current directory!

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

filePLPath = os.path.join(os.path.dirname(filePath), 'webs_pl.txt')
fileOtherPath = os.path.join(os.path.dirname(filePath), 'webs_other.txt')

filePL = open(filePLPath, 'w')
fileOther = open(fileOtherPath, 'w')
                 
for adress in webadresses:

    if adress.endswith('.pl'):
        
        filePL.write(adress + '\n')

    else:

        fileOther.write(adress + '\n')

filePL.close()
fileOther.close()
                 
