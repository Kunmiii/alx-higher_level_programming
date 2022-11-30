#!/usr/bin/python3
a = 97
z = 123
while a < z:
    if (a != 113 and a != 101):
        print("{}".format(chr(a)), end="")
    a += 1
