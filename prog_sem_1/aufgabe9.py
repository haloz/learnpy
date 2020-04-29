"""
Schreiben Sie ein Programm, dass den n-ten Buchstaben des Alphabetes auf dem Bildschirm ausgibt, nachdem es Sie nach
der Zahl n gefragt hat
"""

nth = int(input("Which n-th letter of the alphabet?"))

# see https://realpython.com/python-strings/#built-in-string-functions

print(
    "here is your letter: {}".format(
        chr(nth+64)
    )
)
