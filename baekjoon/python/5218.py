'''
import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    result = []
    str1, str2 = sys.stdin.readline().strip().split()

    str_len = len(str1)

    for i in range(str_len):
        if str1[i] <= str2[i]:
            result.append(ord(str2[i]) - ord(str1[i]))
        else:
            result.append(26 + ord(str2[i]) - ord(str1[i]))

    print("Distances: ", end="")
    for r in result:
        print(r, end=" ")
    print()
'''

import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    str1, str2 = sys.stdin.readline().strip().split()

    result = [
        (ord(str2[i]) - ord(str1[i])) % 26
        for i in range(len(str1))
    ]

    print("Distances: " + " ".join(map(str, result)))
