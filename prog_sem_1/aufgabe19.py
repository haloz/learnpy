"""
Modifizieren Sie Ihr Programm aus der vorangegangen Aufgabe derart, dass das Programm nach der Ausgabe des Maximums den
Benutzer fragt, ob weitere Werte zu bearbeiten sind, und ggf. wieder von vorn beginnt. Nutzen Sie zur Lösung zunächst
die do-Anweisung, dann die while-Anweisung und zum Schluß die for-Anweisung. Machen Sie sich die Unterschiede klar!
"""

import sys

# note: there's no do .. while loop in python. You can do this with a while(true) loop:
while True:
    print("Enter the first number:")
    firstNumber = int(sys.stdin.readline())

    print("Enter the second number:")
    secondNumber = int(sys.stdin.readline())

    # python's ternary operator: https://book.pythontips.com/en/latest/ternary_operators.html

    print(
        "maximum=",
        firstNumber if firstNumber > secondNumber else secondNumber
    )

    print("Do you like to do another round? (y/n)")
    if sys.stdin.readline().rstrip() != "y":   # rstrip strips trailing whitespace/line breaks
        break

# while version

skip = True
while skip:
    print("Enter the first number:")
    firstNumber = int(sys.stdin.readline())

    print("Enter the second number:")
    secondNumber = int(sys.stdin.readline())

    # python's ternary operator: https://book.pythontips.com/en/latest/ternary_operators.html

    print(
        "maximum=",
        firstNumber if firstNumber > secondNumber else secondNumber
    )

    print("Do you like to do another round? (y/n)")
    if sys.stdin.readline().rstrip() != "y":   # rstrip strips trailing whitespace/line breaks
        skip = False


# for version

# does not make sense in python. In contrast to C, there's only a collection-based for loop in python.
# See https://realpython.com/python-for-loop/
