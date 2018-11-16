import os

line = input('How in your opinion is maximum accepted cost of Udemy course? ')

path = input('Enter a file path: ')

try:    
    file = open(path, 'w')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is: ', value)
    
except FileNotFoundError as e:
    print('Error opening file.\n- ', e)

except ValueError as e:
    print('The value entered cannot be converted to a number!\n- ', e)

except:
    print('Something goes wrong...')

else:
    print()
    print('Actions completed successfully')
