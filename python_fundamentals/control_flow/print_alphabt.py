#!/usr/bin/env python3


result = ""
for letter in range(97, 123):
    if letter != 101 and letter != 113:
        result += chr(letter)
print("{}".format(result))
