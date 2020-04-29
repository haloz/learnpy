"""
Erstellen Sie ein Programm, das eine Integerzahl einliest und dann sowohl von dieser als auch von ihren 4 direkten
Nachfolgern die Quadratwurzel berechnet und zusammen mit der Zahl in einer kleinen Tabelle ausgibt. Verwenden Sie zur
Berechnung die Funktion sqrt() der Standardbibliothek math, die im Lehrheft "Kurzbeschreibung ausgewählter
C-Funktionen" beschrieben ist.
"""

import math

number = int(input("Please enter a number:"))

for val in range(number, number+5):
    print("{:<8d} | {:<8.2f}".format(val, math.sqrt(val)))
