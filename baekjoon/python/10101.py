import sys

angle1 = int(sys.stdin.readline())
angle2 = int(sys.stdin.readline())
angle3 = int(sys.stdin.readline())

total_angle = angle1 + angle2 + angle3

if total_angle != 180:
    print("Error")

else:
    if angle1 == 60 and angle2 == 60 and angle3 == 60:
        print("Equilateral")
    elif angle1 in (angle2, angle3) or angle2 == angle3:
        print("Isosceles")
    else:
        print("Scalene")
