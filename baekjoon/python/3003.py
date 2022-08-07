import sys

master_piece = [1, 1, 2, 2, 2, 8]
find_piece = list(map(int, sys.stdin.readline().split()))

for i in range(len(master_piece)):
    print(master_piece[i] - find_piece[i], end=" ")
