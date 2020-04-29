"""
In Analogie zur vorangegangen Wüfel-Aufgabe ist ein Programm für gerade Kreiszylinder zu schreiben, das bei gegebener
(einzugebender) Höhe und Durchmesser
* die Mantelfläche (=pi*d*h),
* Oberfläche (=0.5pi*d*(d+2h)) und
* das Volumen (=0,25*pi*d*d*h) berechnet und ausgibt.
"""

import math

diameter = int(input("Enter the circular cylinder's diameter:"))
height = int(input("Enter the circular cylinder's height:"))

print(
    "Outer surface area: ",
    math.pi * diameter * height,
    "Surface: ",
    0.5 * math.pi * diameter * (diameter + 2 * height),
    "Volume: ",
    0.25 * math.pi * diameter * diameter * height
)
