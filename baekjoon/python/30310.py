import sys

n = int(sys.stdin.readline())

fork_list = list(map(int, sys.stdin.readline().strip().split()))
fork_list.sort()

print(sum(fork_list[:2]))
