import sys
import re

chromosomal_pattern = re.compile("^[A-E]?A+F+C+[A-E]?$")

n = int(sys.stdin.readline())

for _ in range(n):
    if re.match(chromosomal_pattern, sys.stdin.readline().strip()):
        print("Infected!")
    else:
        print("Good")
