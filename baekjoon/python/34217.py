import sys

a, b = map(int, sys.stdin.readline().strip().split())
c, d = map(int, sys.stdin.readline().strip().split())

hanyang = a + c
yongdap = b + d

if hanyang == yongdap:
    print("Either")
elif hanyang < yongdap:
    print("Hanyang Univ.")
else:
    print("Yongdap")
