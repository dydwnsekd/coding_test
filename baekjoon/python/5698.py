import sys

while True:
    s = sys.stdin.readline().strip().lower()

    if s == "*":
        break

    words = s.split()
    w = words[0][0]

    tautogram = True

    for word in words:
        if w != word[0]:
            tautogram = False
            break

    if tautogram:
        print("Y")
    else:
        print("N")
