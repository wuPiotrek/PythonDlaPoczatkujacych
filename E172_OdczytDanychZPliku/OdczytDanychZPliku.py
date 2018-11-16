#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

import os

file_path = r'C:\temp\orders.csv'

with open(file_path, 'r') as file:

    for line in file:
        
        newLine = line.replace('\n', '')
        order = newLine.split(',')
        
        if len(order) == 3:            
            print('Order from drugstore "%s", item "%s", amount %s' \
                  % (order[0], order[1], order[2]))

        else:
            print("Line %s malformed!!!" % (newLine))

print('\nProcessing of file finished!')

#################################################
