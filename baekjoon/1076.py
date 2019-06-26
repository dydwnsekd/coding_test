'''
black	0	1
brown	1	10
red	    2	100
orange	3	1000
yellow	4	10000
green	5	100000
blue	6	1000000
violet	7	10000000
grey	8	100000000
white	9	1000000000
'''

import sys

num_dict = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
last_dict = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000, 'green': 100000, 'blue': 1000000, 'violet': 10000000, 'grey': 100000000, 'white': 1000000000}

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
thrid = sys.stdin.readline().rstrip()

print ('%d' % (int(num_dict[first]+num_dict[second]) * int(last_dict[thrid])))