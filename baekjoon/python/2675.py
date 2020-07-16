import sys

num = int(sys.stdin.readline().split()[0])

for i in range(num):
    n, input_str = sys.stdin.readline().split()

    n = int(n)
    
    for j in range(len(input_str)):
        print(input_str[j]*n, end="")

    print()