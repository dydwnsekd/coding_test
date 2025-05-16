import sys

n = int(sys.stdin.readline())
upper_alphabet = []

for i in range(ord("A"), ord("Z") + 1):
    upper_alphabet.append(chr(i))

for _ in range(n):
    s = sys.stdin.readline().strip()
    result = ""

    for c in s:
        if c in upper_alphabet:
            result += "_" + c.lower()
        else:
            result += c

    print(result)


