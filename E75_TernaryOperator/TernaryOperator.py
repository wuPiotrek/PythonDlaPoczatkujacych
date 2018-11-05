#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

# Warunki wejściowe:
musclePain = True
fever = False
weakness = False
# -
print('musclePain \t', musclePain)
print('fever \t\t', fever)
print('weakness \t', weakness)

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

print("suspiction of influenza" if (musclePain and fever and weakness) else "The flu is unlikely")

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

if (musclePain and fever and weakness):
    print("suspiction of influenza")
elif weakness and (not fever or not musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")

#################################################
exNumber = 4, 5
print("-" * 5, exNumber, "-" * 25)
# Code:

# Warunki wejściowe:
isMan = True
# -
if (musclePain and fever and weakness) or ((musclePain or fever or weakness) and isMan):
    print("suspiction of influenza")
elif weakness and (not fever or not musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")

#################################################
exNumber = 6
print("-" * 5, exNumber, "-" * 30)
# Code:

# Warunki wejściowe:
isCheckCompleted = False
# -
print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")
