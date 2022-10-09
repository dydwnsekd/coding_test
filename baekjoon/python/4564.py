import sys

while True:
    n = sys.stdin.readline().strip()
    if n == "0":
        break
    else:
        while True:
            temp_value = 1
            if len(n) == 1:
                print(n)
                break
            else:
                for i in n:
                    temp_value *= int(i)
                    n = str(temp_value)
                print(temp_value, end=" ")
0
