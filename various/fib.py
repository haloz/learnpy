# multiple assignment in one line
a, b = 0, 1
while(b < 100):
    print(b)
    # here again to switch the values. A statement like a, b = b, a is
    # perfectly valid. You can switch two variable values without needing a
    # third as temporary one.
    a, b = b, a+b
