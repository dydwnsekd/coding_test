import sys

buger_list = list()
drink_list = list()

for i in range(3):
    buger_list.append(int(sys.stdin.readline()))

for i in range(2):
    drink_list.append(int(sys.stdin.readline()))

print (min(buger_list) + min(drink_list) - 50)