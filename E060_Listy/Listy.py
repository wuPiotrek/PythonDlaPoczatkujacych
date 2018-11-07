#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsTitles = [ 'BROTHERS IN ARMS', \
               'BOHEMIAN RHAPSODY', \
               'STAIRWAY TO HEAVEN', \
               'RIDERS ON THE STORM', \
               'WISH YOU WERE HERE']
print(hitsTitles)

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
print(hitsTitles)

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsTitles[2] = 'HOTEL CALIFORNIA'
print(hitsTitles)

#################################################
exNumber = 4
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles)

#################################################
exNumber = 5
print("-" * 5, exNumber, "-" * 30)
# Code:

print(hitsTitles.index('HOTEL CALIFORNIA'))

#################################################
exNumber = 6
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsTitles.remove('HOTEL CALIFORNIA')
print(hitsTitles)

#################################################
exNumber = 7
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsTitles[0] = "ENJOY THE SILENCE"
print(hitsTitles)

#################################################
exNumber = 8
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsToRead = hitsTitles.copy()
print(hitsToRead)

#################################################
exNumber = 9
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsToRead.reverse()
print(hitsToRead)

#################################################
exNumber = 10
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsToRead.sort()
print(hitsToRead)

#################################################
exNumber = 11
print("-" * 5, exNumber, "-" * 30)
# Code:

print(hitsToRead)
print()
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))
print()
print(hitsToRead)

#################################################
exNumber = 12
print("-" * 5, exNumber, "-" * 30)
# Code:

additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
print(additionalSongs)

#################################################
exNumber = 13
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsToRead.extend(additionalSongs)
print(hitsToRead)

#################################################
exNumber = 14
print("-" * 5, exNumber, "-" * 30)
# Code:

print('WISH YOU WERE HERE:', hitsToRead.count('WISH YOU WERE HERE'))
print('RIDERS ON THE STORM:', hitsToRead.count('RIDERS ON THE STORM'))

#################################################
exNumber = 15
print("-" * 5, exNumber, "-" * 30)
# Code:

hitsToRead.clear()
print(hitsToRead)
#print(hitsTitles)

#################################################
