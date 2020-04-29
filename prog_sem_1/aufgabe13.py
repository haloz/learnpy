"""
Würfel
Erstellen Sie ein Programm zur Berechnung von Eigenschaften eines Würfels, das bei gegebener (d.h. in Ihrem Fall
einzugebender) Kantenlänge a
* den Flächenumfang (=6a*a),
* das Volumen (=a*a*a) und
* die Länge der Raumdiagonale (=a*sqrt(3))
berechnet und ausgibt.
"""

import math

sideLength = int(input("Please specify the side length of the cube:"))

print(
    "Surface area: ",
    6 * sideLength * sideLength,
    "Volume: ",
    sideLength * sideLength * sideLength,
    "Length of the space diagonal: ",
    sideLength * math.sqrt(3)
)
