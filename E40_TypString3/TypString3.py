article = '''Latający cyrk Monty Pythona – komediowy serial telewizyjny tworzony przez grupę
brytyjskich komików, Monty Python. Producentami i reżyserami serialu byli Ian MacNaughton
i John Howard Davies.
'''
print(article.upper())
print()
print(article.lower().replace("monty", "flying"))
print()
print(article.split(" "))
print()
print("word python appears", article.lower().count("python"), "times")
print()
print("to print the \\ you need to put \\ twice in your text like this: \\\ ")
print()
print('The best hits of \'80s!!!')
print()
print("The best hits of '80s!!!")
print()

amountPLN = 234
EUR = 4.23
USD = 3.65
print("cur\texchange\tamount")
print("USD'\t", USD, "\t", "\t", (amountPLN / USD), sep="")
print("EUR'\t", EUR, "\t", "\t", (amountPLN / EUR), sep="")
print()


ValueAsText = '123.45'
factor = 1.23
print("value is", ValueAsText, "factor is", factor, "value*factor=", (float(ValueAsText) * factor))
