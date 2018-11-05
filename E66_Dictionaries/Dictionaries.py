#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

channels  = {'Google':1480, 'Email':300, 'Natural Traffic':440, 'TV Spot':700}
print(channels)

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

print(channels['Email'])

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

channelsUpdate = {'Natural Traffic':520, 'News':600}
print(channelsUpdate)

#################################################
exNumber = 4
print("-" * 5, exNumber, "-" * 30)
# Code:

channels.update(channelsUpdate)
print(channels)

#################################################
exNumber = 5
print("-" * 5, exNumber, "-" * 30)
# Code:

print(channels.keys())

#################################################
exNumber = 6
print("-" * 5, exNumber, "-" * 30)
# Code:

channels.pop('Email')
print(channels)

#################################################
