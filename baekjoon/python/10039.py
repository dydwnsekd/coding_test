import sys

num = 0

for _ in range(5):
    
    n = int(sys.stdin.readline())
    if n<40:
        num += 40
    else:
        num += n

print (int(num/5)) 