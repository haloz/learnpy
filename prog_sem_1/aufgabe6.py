"""
Schreiben Sie ein Programm, dass Sie nacheinander zur Eingabe von 2 Integerzahlen auffordert, die von Ihnen
eingegebenen Zahlen auf zwei Variablen vom Typ int abspeichert und danach die Summe, die Differenz, das Produkt und den
Quotienten ausgibt.
"""

firstNumber = int(input("Please enter the 1st number:"))
secondNumber = int(input("Please enter the 2nd number:"))

print("{}+{} = {}".format(
    firstNumber, secondNumber,
    firstNumber+secondNumber)
)

print("{}-{} = {}".format(
    firstNumber, secondNumber,
    firstNumber-secondNumber)
)

print("{}*{} = {}".format(
    firstNumber, secondNumber,
    firstNumber*secondNumber)
)

print("{}/{} = {}".format(
    firstNumber, secondNumber,
    firstNumber/secondNumber)
)
