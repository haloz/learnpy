"""
Aufgabe 14: ein einfaches Zahlenspiel
Der Computer "merkt" sich eine Zufallszahl zwischen 1 und 15, die der Spieler (=Benutzer) erraten soll. Der Spieler hat
insgesamt drei Versuche. Nach jedem falschen Versuch gibt der Computer an, ob die angegebene Zahl zu klein oder zu groß
ist. Ist auch der 3. Versuch erfolglos, wird die gesuchte Zahl ausgegeben. Der Spieler hat gewonnen, wenn er innerhalb
der 3 Versuche, die Zahl errät. Er soll das Spiel beliebig oft wiederholen können. Hinweis: Zur Initialisierung des
Zufallszahlengenerators verwenden Sie die Systemzeit.
  #include <time.h>                    /* Prototyp von time() */
  #include <stdlib.h>    /* Prototypen von srand() und rand() */
  ...
  long sek;     /* für Speicherung der Sekunden seit 1.1.1970 */
  ...
  time(&sek);                    /* Anzahl der Sekunden holen */
  srand(sek);            /* und zur Initialisierung verwenden */
"""

import random
import sys

playAgain = True
numberOfRightGuesses = 0
numberOfGames = 0

while playAgain:
    numberOfGames += 1
    randomNumber = random.randrange(1, 16)
    print("I picked a number in range from 1 to 15. Guess what my number is! You have 3 trys!")

    won = False
    for trial in range(1, 4):
        print("{}. Try:".format(trial))
        try:
            guess = int(sys.stdin.readline().rstrip())
        except ValueError:
            print("What? That's not a number. Next try...")
            continue
        if guess == randomNumber:
            won = True
            break
        else:
            print("nope! ", end='')
            print("hint:", "my number is higher!" if randomNumber > guess else "my number is lower!")

    if won:
        print("Congrats! You're right!")
        numberOfRightGuesses += 1
    else:
        print("Boo! Better luck next time! My number was", randomNumber)

    print("Play again? (y/n)")
    if sys.stdin.readline().rstrip() == "n":
        playAgain = False

print("You won {} out of {} games. Thank you!".format(numberOfRightGuesses, numberOfGames))
