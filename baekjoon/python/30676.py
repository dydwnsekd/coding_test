# commit 대기(init)
import sys

n = int(sys.stdin.readline())

if 380 <= n < 425:
    print("Violet")
elif n < 450:
    print("Indigo")
elif n < 495:
    print("Blue")
elif n < 570:
    print("Green")
elif n < 590:
    print("Yellow")
elif n < 620:
    print("Orange")
elif n < 780:
    print("Red")
