import sys


def case_converter(s: str):
    coefficient = 32
    if 65 <= ord(s) <= 90:
        return chr(ord(s) + coefficient)
    elif 97 <= ord(s) <= 122:
        return chr(ord(s) - coefficient)


s = input()
convert_s = ""

for i in s:
    convert_s += case_converter(i)

print(convert_s)

