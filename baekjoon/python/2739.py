import sys

a = sys.stdin.readline()
a = int(a)

for i in range(1, 10):
    print ('%d * %d = %d' % (a,i,a*i))