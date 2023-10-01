import sys

while True:
    words = sys.stdin.readline().rstrip()
    if words == "#":
        break

    for word in words.split(" "):
        print(word[::-1], end=" ")
    print()
