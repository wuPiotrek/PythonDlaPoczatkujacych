#################################################
exNumber = '1 - 2'
print("-" * 5, exNumber, "-" * 30)
# Code:

import os
import time

enteredDir = input('Plese enter a file directory: ')

#################################################
exNumber = '3 - 7'
print("-" * 5, exNumber, "-" * 30)
# Code:

if not os.path.isdir(enteredDir):

    print('This is not directory!')

else:

    file = input('Please enter file name: ')
    path = os.path.join(enteredDir, file)

    if not os.path.exists(path):

        print('File does not exist!')
        
    else:
        
        print('\nProperties of file below:')
        print('\nLast modify date is:', time.asctime(time.localtime(os.path.getmtime(path))))
        print('The file size [B] is:', os.path.getsize(path))
        print('Current directory is:', os.getcwd())
        print('Relative directory:', os.path.relpath(path))
             
#################################################

