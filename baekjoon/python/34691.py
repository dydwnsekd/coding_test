import sys

while True:
    s = sys.stdin.readline().strip()
    if s == "end":
        break
    elif s == "animal":
        print("Panthera tigris")
    elif s == "flower":
        print("Forsythia koreana")
    elif s == "tree":
        print("Pinus densiflora")
