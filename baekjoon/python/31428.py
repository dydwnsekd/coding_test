import sys

n = int(sys.stdin.readline())
friends = sys.stdin.readline().strip().split()
alice = sys.stdin.readline().strip()

print(friends.count(alice))
