# The application is indended to create a *.txt file with the addresses
# of webpages typed by user.
# The file will be created in current directory!

import os

print('Type a web adress and press enter. To stop typing press enter without writing an adress')
print()

webAdresses = []

line = input('Enter webpage adress: ')

while line:
    
    webAdresses.append(line)
    line = input('Enter webpage adress: ')

dirName = os.getcwd()
print()
fileName = input('Enter name of the file: ')
filePath = os.path.join(dirName, fileName + '.txt')

file = open(filePath, 'w')

for adress in webAdresses:

    file.write(adress + '\n')

file.close()
print()
print('File '+ fileName + '.txt is successful saved in current directory!')
