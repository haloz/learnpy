"""
Die Fibonacci-Zahlen sind wie folgt definiert:
   fib(0)=0;
   fib(1)=1;
   fib(i)=fib(i-1)+fib(i-2)    für 2<=i<=n
Berechnen Sie mit Hilfe der oben genannten rekusiven Definition zyklisch die ersten n Fibonacci-Zahlen
(eine Zahl n>=0 ist vom Nutzer zu erfragen).
Erhöhen Sie die Effizienz Ihres Programms, indem Sie anstatt der Rekursion mit einer for-Schleife arbeiten.
"""

import sys

print("Up to which n-th fibonacci number?")
n = int(sys.stdin.readline().rstrip())

# using recursion


def fib(number, maximum):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number <= maximum:
        return fib(number - 1, maximum) + fib(number - 2, maximum)


print(fib(n, n))

# using a loop

lastNumber = 0
lastLastNumber = 1
result = 0
for number in range(1, n):
    result = lastNumber + lastLastNumber
    lastNumber = lastLastNumber
    lastLastNumber = result

print(result)