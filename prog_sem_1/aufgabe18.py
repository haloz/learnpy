"""
Maximum
Schreiben Sie ein Programm, dass zwei int-Werte von der Tastatur einliest und mit Hilfe der if-Anweisung das Maximum
dieser zwei Werte bestimmt und ausgibt.
"""

import sys

print("Enter the first number:")
firstNumber = int(sys.stdin.readline())

print("Enter the second number:")
secondNumber = int(sys.stdin.readline())

# python's ternary operator: https://book.pythontips.com/en/latest/ternary_operators.html

print(
    "maximum=",
    firstNumber if firstNumber > secondNumber else secondNumber
)
