import sys

n = int(sys.stdin.readline())
upper_alphabet = []

for i in range(ord("A"), ord("Z") + 1):
    upper_alphabet.append(chr(i))

for _ in range(n):
    s = sys.stdin.readline().strip()
    result = s[0].lower()

    for c in s[1:]:
        if c in upper_alphabet:
            result += "_" + c.lower()
        else:
            result += c

    print(result)


