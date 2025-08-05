import sys

n = int(sys.stdin.readline())

receipt = sys.stdin.readline().strip().split(' ')
ingredient = sys.stdin.readline().strip().split(' ')

for r in receipt:
    if r not in ingredient:
        print(r)
        break

