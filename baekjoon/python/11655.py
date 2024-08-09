import sys

result = ""

capital = [i for i in range(65, 91)]
rot_capital = []
small_letter = [i for i in range(97, 123)]
rot_small_letter = []
c = ord("z") - ord("a") + 1

s = sys.stdin.readline()

for i in s:
    if ord("A") <= ord(i) <= ord("Z"):
        if ord(i) + 13 > ord("Z"):
            result += chr(ord(i) + 13 - c)
        else:
            result += chr(ord(i) + 13)
    elif ord("a") <= ord(i) <= ord("z"):
        if ord(i) + 13 > ord("z"):
            result += chr(ord(i) + 13 - c)
        else:
            result += chr(ord(i) + 13)
    else:
        result += i

print(result)

