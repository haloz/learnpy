"""
Dividieren Sie zwei Integerzahlen, die Sie von der Tastatur eingelesen haben, einmal mit und einmal ohne erzwungene
Typumwandlung zur Gleitkommazahl und speichern Sie das Ergebnis jeweils auf eine Variable vom Typ float. Geben Sie das
Ergebnis aus und erklären sich die Abweichung der beiden Werte, wenn die eine Integerzahl nicht durch die andere
teilbar ist.
"""

import sys

numberOne = int(sys.stdin.readline())
numberTwo = int(sys.stdin.readline())

floatDivided = numberOne / numberTwo  # default is to convert to float, no need to cast
intDivided = int(numberOne / numberTwo)  # explicit int cast caps fragment

print("int divided = {}, float divided = {}".format(intDivided, floatDivided))
