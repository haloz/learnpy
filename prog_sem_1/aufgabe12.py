"""
Schreiben Sie ein Programm, das von Ihnen einen float-Wert einliest, von diesem Wert 1 subtrahiert und das Ergebnis als
float-Wert wieder ausgibt. Geben Sie nach Abfrage durch das Programm den Wert 1.23456e10 ein. Welches Ergebnis erwarten
Sie, wenn Ihr Programm eine Millionen mal die 1 von Ihrem Wert subtrahieren würde?
"""

import sys

print("please enter a floating point number:")
floatValue = float(sys.stdin.readline())

print("my value = ", floatValue)
print("my value minus 1 = ", floatValue - 1)
print("my value minus 1.0 = ", floatValue - 1.0)
