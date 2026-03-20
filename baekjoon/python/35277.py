import sys

kadayif = 900
butter = 60
pistachio = 600
white_chocolate = 170
marshmallow = 160
cocoa_powder = 110

duzzoncu_price = kadayif + butter + pistachio + white_chocolate + marshmallow + cocoa_powder
n = int(sys.stdin.readline())

print(n // duzzoncu_price)
