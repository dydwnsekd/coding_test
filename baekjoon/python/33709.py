"""
import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().replace('|', '.').replace(':', '.').replace('#', '.').split('.')))

print(sum(num_list))
"""

import re
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, re.split(r'[.|:#]', sys.stdin.readline().strip())))

print(sum(numbers))
