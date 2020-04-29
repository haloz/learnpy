"""
Ändern Sie das Programm aus Aufgabe 1, indem Sie Gleitkommazahlen für Eingabe und Ausgabe verwenden.
"""

import sys

print("Please enter the 1st number:")
firstNumber = float(sys.stdin.readline())

print("Please enter the 2nd number:")
secondNumber = float(sys.stdin.readline())

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
