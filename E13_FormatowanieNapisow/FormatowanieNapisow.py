helloMessage = "Hello %s!"
print(helloMessage % 'Kate')
print(helloMessage % 'Chris')
print()
helloMessage = "Hello {0:s}!"
print(helloMessage.format('Kate'))
print(helloMessage.format('Chris'))
print()
helloMessage = "%s has %d %s"
print(helloMessage % ('Kate', 1, 'animal'))
print(helloMessage % ('Chris', 100000, '$'))
print()
helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format('Kate', 1, 'animal'))
print(helloMessage.format('Chris', 100000, '$'))
print()
line = '{0:20s} costs {1:6d} €'
print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAI', 6))
