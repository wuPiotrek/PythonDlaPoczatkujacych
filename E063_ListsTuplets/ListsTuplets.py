#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

marketing = ['loyality program', 'client promotion', 'market research']
print(marketing)

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

marketing.append('public relations')
print(marketing)

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

print(marketing[2])

#################################################
exNumber = 4
print("-" * 5, exNumber, "-" * 30)
# Code:

marketing.insert(1, 'investor relations')
print(marketing)

#################################################
exNumber = 5
print("-" * 5, exNumber, "-" * 30)
# Code:

emailMarketing = marketing.copy()
print(emailMarketing)

#################################################
exNumber = 6
print("-" * 5, exNumber, "-" * 30)
# Code:

emailMarketing.sort()
print(emailMarketing)

#################################################
exNumber = 7
print("-" * 5, exNumber, "-" * 30)
# Code:

internalEmails = ['internal communication']
print(internalEmails)

#################################################
exNumber = 8
print("-" * 5, exNumber, "-" * 30)
# Code:

emailMarketing.extend(internalEmails)
print(emailMarketing)

#################################################
exNumber = 9
print("-" * 5, exNumber, "-" * 30)
# Code:

emailMarketingTuple = tuple(emailMarketing)
print(emailMarketingTuple)

#################################################
