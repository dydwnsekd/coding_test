import sys

while True:
    n = sys.stdin.readline().strip()
    if n == "0":
        break
    else:
        print(n, end=" ")
        while True:
            temp_value = 1
            if len(n) == 1:
                print()
                break
            else:
                for i in n:
                    temp_value *= int(i)
                    n = str(temp_value)
                print(n, end=" ")
