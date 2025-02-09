import sys

weight = float(sys.stdin.readline())
height = float(sys.stdin.readline())

BMI = weight / (height ** 2)

if BMI < 18.5:
    print("Underweight")
elif BMI <= 25:
    print("Normal weight")
else:
    print("Overweight")

