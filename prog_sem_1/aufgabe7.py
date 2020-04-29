"""
Ändern Sie das Programm aus Aufgabe 1, indem Sie Gleitkommazahlen für Eingabe und Ausgabe verwenden.
"""

firstNumber = float(input("Please enter the 1st number:"))
secondNumber = float(input("Please enter the 2nd number:"))

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
