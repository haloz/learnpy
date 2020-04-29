"""
Schreiben Sie ein Programm, dass Sie nacheinander zur Eingabe von 2 Integerzahlen auffordert, die von Ihnen
eingegebenen Zahlen auf zwei Variablen vom Typ int abspeichert und danach die Summe, die Differenz, das Produkt und den
Quotienten ausgibt.
"""

import sys

print("Please enter the 1st number:")
firstNumber = int(sys.stdin.readline())

print("Please enter the 2nd number:")
secondNumber = int(sys.stdin.readline())

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
