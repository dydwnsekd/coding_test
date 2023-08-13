import sys

a, b = list(map(int, sys.stdin.readline().split()))
m = (b-a)/400

print(1/(1+pow(10, m)))
