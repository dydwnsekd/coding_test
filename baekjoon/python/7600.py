import sys

while True:
    alphabet_set = []
    s = sys.stdin.readline().strip().replace(" ", "").lower()
    if s == "#":
        break

    for i in s:
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            alphabet_set.append(ord(i))

    print(len(set(alphabet_set)))
