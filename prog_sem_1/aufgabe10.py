"""
Lesen Sie 3 Zahlen, eine vom Typ int, eine vom Typ long und eine vom Typ float, von der Tastatur ein. Speichern Sie die
Summe der 3 Zahlen jeweils auf eine Variable vom Typ int, eine vom Typ long und eine vom Typ float ab und geben Sie die
Werte auf dem Bildschirm aus. Erklären Sie sich die unterschiedlichen Ergebnisse.
"""

import sys

print("Please enter an (integer) number:")
numberOfTypeInt = int(sys.stdin.readline())

print("Please enter an (float) number:")
numberOfTypeFloat = float(sys.stdin.readline())

intSum = int(numberOfTypeInt + numberOfTypeFloat)
floatSum = float(numberOfTypeInt + numberOfTypeFloat)
print("int sum = {}, float sum = {}".format(intSum, floatSum))
