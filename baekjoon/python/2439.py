import sys

a = sys.stdin.readline()
a = int(a)

for i in range(1, a+1):
    p = '%s%s' % (' '* int(a-i), '*' * i)

    print (p)