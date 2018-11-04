#1
marketing = ['loyality program', 'client promotion', 'market research']
print(marketing)
#2
marketing.append('public relations')
print(marketing)
print()
#3
print('Pozycja numer 3:')
print(marketing[2])
print()
#4
marketing.insert(2, 'investor relations')
print(marketing)
print()
#5
emailMarketing = marketing.copy()
print(emailMarketing)
print()
#6
emailMarketing.sort()
print(emailMarketing)
print()
#7
internalEmails = ['internal communication']
print(internalEmails)
print()
#8
emailMarketing.extend(internalEmails)
print(emailMarketing)
print()
#9
emailMarketingTuple = tuple(emailMarketing)
print(emailMarketingTuple)
print(type(emailMarketingTuple))
