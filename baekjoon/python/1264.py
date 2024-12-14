import sys

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    s = sys.stdin.readline().strip()

    if s == "#":
        break

    s = s.lower()

    count = 0

    for i in range(len(s)):
        if s[i] in vowel:
            count += 1

    print(count)
