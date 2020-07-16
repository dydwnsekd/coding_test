import sys

while True:
    num1, num2 = list(map(int, sys.stdin.readline().split(" ")))

    if num1 == 0 and num2 == 0:
        break
    
    print (num1+num2)