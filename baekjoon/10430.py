import sys

a, b, c = sys.stdin.readline().split()

a = int(a)
b = int(b)
c = int(c)

print (int((a+b)%c))
print (int((a%c + b%c)%c))
print (int((a*b)%c))
print (int(a%c * b%c) % c)