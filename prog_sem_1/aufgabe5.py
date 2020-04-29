"""
Erweitern Sie das Programm aus Aufgabe 4 indem Sie sich zusätzlich die Gleitkommakonstante pi mit dem Wert 3.1415926
definieren, jeden Wert in der Tabelle vor seiner Ausgabe mit pi multiplizieren und das Ergebnis als Gleitkommazahl
ebenfalls mit Tabulatoren und 3 Ausgabeanweisungen tabellarisch darstellen.
"""

pi = 3.1415926
formatting = "{:<8.2f}{:<8.2f}{:<8.2f}{:<8.2f}"
print(formatting.format(pi, 2 * pi, 3 * pi, 4 * pi))
print(formatting.format(2 * pi, 4 * pi, 6 * pi, 8 * pi))
print(formatting.format(3 * pi, 6 * pi, 9 * pi, 12 * pi))
