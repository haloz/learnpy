"""
Modifizieren Sie Ihr Programm aus der vorangegangen Aufgabe derart, dass das Programm nach der Ausgabe des Maximums den
Benutzer fragt, ob weitere Werte zu bearbeiten sind, und ggf. wieder von vorn beginnt. Nutzen Sie zur Lösung zunächst
die do-Anweisung, dann die while-Anweisung und zum Schluß die for-Anweisung. Machen Sie sich die Unterschiede klar!
"""

# note: there's no do .. while loop in python. You can do this with a while(true) loop:

while True:
    firstNumber = int(input("Enter the first number:"))
    secondNumber = int(input("Enter the second number:"))

    # python's ternary operator: https://book.pythontips.com/en/latest/ternary_operators.html

    print(
        "maximum=",
        firstNumber if firstNumber > secondNumber else secondNumber
    )

    if input("Do you like to do another round? (y/n)") != "y":
        break

# while version

skip = True
while skip:
    firstNumber = int(input("Enter the first number:"))
    secondNumber = int(input("Enter the second number:"))

    # python's ternary operator: https://book.pythontips.com/en/latest/ternary_operators.html

    print(
        "maximum=",
        firstNumber if firstNumber > secondNumber else secondNumber
    )

    if input("Do you like to do another round? (y/n)") != "y":
        skip = False


# for version

# does not make sense in python. In contrast to C, there's only a collection-based for loop in python.
# See https://realpython.com/python-for-loop/
