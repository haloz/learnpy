"""
Maximum
Schreiben Sie ein Programm, dass zwei int-Werte von der Tastatur einliest und mit Hilfe der if-Anweisung das Maximum
dieser zwei Werte bestimmt und ausgibt.
"""

import sys

firstNumber = int(input("Enter the first number:"))
secondNumber = int(input("Enter the second number:"))

# python's ternary operator: https://book.pythontips.com/en/latest/ternary_operators.html

print(
    "maximum=",
    firstNumber if firstNumber > secondNumber else secondNumber
)
