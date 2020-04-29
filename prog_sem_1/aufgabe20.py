"""
Die Fibonacci-Zahlen sind wie folgt definiert:
   fib(0)=0;
   fib(1)=1;
   fib(i)=fib(i-1)+fib(i-2)    für 2<=i<=n
Berechnen Sie mit Hilfe der oben genannten rekusiven Definition zyklisch die ersten n Fibonacci-Zahlen
(eine Zahl n>=0 ist vom Nutzer zu erfragen).
Erhöhen Sie die Effizienz Ihres Programms, indem Sie anstatt der Rekursion mit einer for-Schleife arbeiten.
"""

n = int(input("Up to which n-th fibonacci number?"))


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

# using multiple assignment in one line

lastNumber = 0
lastLastNumber = 1
for number in range(1, n):
    lastNumber, lastLastNumber = lastLastNumber, lastNumber + lastLastNumber

print(lastLastNumber)


max_fib_number = 10000000

# a function that creates and returns a list of fib numbers up to given max. The caller of the function has to wait
# until the whole function is done filling the list. Without a max this would run until out of memory.

def fib_classical(max):
    nums = []
    current, nxt = 0, 1
    while current < max:
        current, nxt = nxt, nxt + current
        nums.append(current)

    return nums

print("classic:")
for item in fib_classical(max_fib_number):
    print(item, end=", ")
print()


# generator version. this will "run forever" and never crash out of memory.

def fib_generator():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, nxt + current
        yield current

print("generator:")
for next_number in fib_generator():
    print(next_number, end=", ")
    if next_number > max_fib_number:
        break
print()

# we can even compose this ;) This new generator reuses the former generator, yielding only the even numbers that it
# received

def fib_even_numbers():
    for n in fib_generator():
        if n % 2 == 0:
            yield n

print("evens:")
for next_number in fib_even_numbers():
    print(next_number, end=", ")
    if next_number > max_fib_number:
        break
print()

# composed with another one

def fib_divisible_by_three():
    for n in fib_even_numbers():
        if n % 3 == 0:
            yield n

print("evens, divisible by 3:")
for next_number in fib_divisible_by_three():
    print(next_number, end=", ")
    if next_number > max_fib_number:
        break
print()
