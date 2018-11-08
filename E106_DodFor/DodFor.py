#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

fibonacciiterations = 20

a1 = 0
a2 = 1
a3 = 0

for i in range(1, fibonacciiterations + 1):

    print('%2d element ciągu:' % (i), a3)
    
    a1 = a2
    a2 = a3
    a3 = a1 + a2
    
#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:    

text = '''\
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.\
'''

textTMP = text.replace('\n', ' ').split(' ')

for item in textTMP:
    
    if 'p' in item.lower():
        
        print(item)
        
#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code: 

dictionary = {'A':'80%-100%', 'B':'60%-80%', 'C':'50-60%', 'D':'less then 50%'}

for x, y in dictionary.items():
    
    print('%s - %s' % (x, y))

#################################################
exNumber = 4
print("-" * 5, exNumber, "-" * 30)
# Code:

wordDictionary = {}
listOfWords = text.lower().replace('\n', ' ')\
              .replace(',', '')\
              .replace('.', '')\
              .replace(':', '')\
              .split(' ')

for word in listOfWords:
    
    if word in wordDictionary.keys():
        wordDictionary[word] += 1
    else:
        wordDictionary[word] = 1

print(wordDictionary)

#################################################
