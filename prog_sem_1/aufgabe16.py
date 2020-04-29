"""
Operatorprioritäten
Wie werden die Operanden und Operatoren im folgenden Ausdruck zusammengefaßt?
  x = -4 * ++i - 6 % 4
Setzen Sie entsprechende Klammern und überprüfen Sie, ob das Programm noch den gleichen Wert für x ermittelt.
"""


i = 5
# x = -4 * ++i - 6 % 4

# 1. ++ operator does not behave the same in python as in C.
#    In C this would increase to 6 before using it in the statement.
#    In python the +/++ is just the identity operator which does nothing here. Also, integers are immutable in
#    python. You have to reassign them to change them.
#    (see https://stackoverflow.com/questions/1485841/behaviour-of-increment-and-decrement-operators-in-python)

# So, instead of:
# x = -4 * ++i - 6 % 4

# we need sth like this:
i += 1
x = -4 * i - 6 % 4

# 2. -4*i = -4*6 = -24
print("-4*i=", -4*i)

# 3. 6%4 = 2
print("6%4=", 6 % 4)

# 4. -24-2 = -26
print("x=", x)
