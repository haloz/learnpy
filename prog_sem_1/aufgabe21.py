"""
Aufgabe 13: Das "kleine Einmaleins"
Schreiben Sie ein Programm, welches das "kleine Einmaleins" in einer Tabelle (wie unten angegeben) vollständig auf dem
Bildschirm ausgibt.
      *******  DAS KLEINE EINMALEINS *******

      1   2   3   4   5   6   7   8   9   10
   1  1   2   3   .   .   .   .   .   .   .
   2  2   4   6   .   .   .   .   .   .   .
   3  3   6   9   .   .   .   .   .   .   .
   4  .   .   .   .   .   .   .   .   .   .
   5  .   .   .   .   .   .   .   .   .   .
   6  .   .   .   .   .   .   .   .   .   .
   7  .   .   .   .   .   .   .   .   .   .
   8  .   .   .   .   .   .   .   .   .   .
   9  .   .   .   .   .   .   .   .   .   .
  10  .   .   .   .   .   .   .   .   .   .
"""

print("      *******  DAS KLEINE EINMALEINS *******")
print("  ", end='')
for column in range(1, 11):
    print("{:5d}".format(column), end='')
print("")

for row in range(1, 11):
    print("{:2d}".format(row), end='')
    for column in range(1, 11):
        print("{:5d}".format(row * column), end='')
    print("")
