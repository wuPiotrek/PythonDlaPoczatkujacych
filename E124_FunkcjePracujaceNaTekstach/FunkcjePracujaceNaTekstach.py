#################################################
exNumber = 1
print("-" * 5, exNumber, "-" * 30)
# Code:

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

print(poem)

#################################################
exNumber = 2
print("-" * 5, exNumber, "-" * 30)
# Code:

lines = poem.split('\n')

print(lines)

#################################################
exNumber = 3
print("-" * 5, exNumber, "-" * 30)
# Code:

i = 0

while i + 8 < len(lines) :
    print(lines[i])
    print(lines[i + 8])
    i += 1

#################################################
