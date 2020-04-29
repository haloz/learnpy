"""
Logische Ausdrücke
Schreiben Sie ein Programm mit dessen Hilfe Sie für eine Integerkonstante x=7 den Wert der folgenden logischen Ausdrücke
berechnen und anzeigen können. Erklären Sie sich die ermittelten Ausgaben!
  x < 9 && x >= -5
  !x && x >= 3
  x++ == 8 || x == 7
"""

x = 7

print(
    "1st expression:",
    9 > x >= -5  # note: && is and in python
)

print(
    "2nd expression:",
    not x and x >= 3   # note: ! is not
)

print(
    "3rd expression:",
    x == 8 or x == 7   #
)
