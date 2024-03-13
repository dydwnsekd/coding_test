import sys

axel, petra = map(int,sys.stdin.readline().split())

axel_value = axel * 7
petra_value = petra * 13

if axel_value > petra_value:
    print("Axel")
elif axel_value == petra_value:
    print("lika")
else:
    print("Petra")
