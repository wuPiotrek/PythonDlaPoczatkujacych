name = "Piotr"
age = 25
daysInYear = 365
message = '%s is %d years old, so is about %d days old'
print(message % (name, age, (daysInYear * age)))
name = "Tomek"
age = 30
daysInYear = 365
print(message % (name, age, (daysInYear * age)))
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format('Chris', 17, 6205))
a = 1234567890
b = 12345
divideResult = a // b
divideRest = a % b
print(a, "divided by", b, "is", divideResult, "and the rest is", divideRest)
