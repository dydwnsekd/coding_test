import sys

x, y = map(int, sys.stdin.readline().split())

chicken = (4 * x - y) // 2
cow = x - chicken

print(chicken, cow)
