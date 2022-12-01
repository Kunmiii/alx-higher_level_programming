#!/usr/bin/python3
def uppercase(str):
    for i in range(1):
        if (ord(tmp[i]) > 96 and ord(tmp[i]) < 123):
            tmp[i] = chr(ord(tmp[i]) - 32)
            print("{}".format(("").join(tmp)))
