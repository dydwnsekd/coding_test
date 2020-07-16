import sys
import math

print ("주 단위 납입금액 입력(n원씩 증액)")
money = int(sys.stdin.readline())
print ("이율 입력")
interest_rate = float(sys.stdin.readline())

total = 0

for i in range(1, 27):
    total += money * i

print ("원금 : %d" % round(total, 1))
print ("이자 포함 총금액(세전) : %d" % round(total + total * (interest_rate / 100), 1))
print ("이자 : %d" % round(total * (interest_rate / 100), 1))