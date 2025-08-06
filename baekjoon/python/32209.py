"""
import sys

q = int(sys.stdin.readline())
questions = 0
flag = True

for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())

    if x == 1:
        questions += y
    if x == 2:
        if questions < y:
            flag = False
            break
        else:
            questions -= y

if flag:
    print("See you next month")
else:
    print("Adios")
"""

import sys

q = int(sys.stdin.readline())
questions = 0

for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())

    if x == 1:
        questions += y
    elif x == 2:
        if questions < y:
            print("Adios")
            break
        questions -= y
else:
    print("See you next month")

