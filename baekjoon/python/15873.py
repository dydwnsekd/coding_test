import sys

nums = sys.stdin.readline().strip()

if nums.count('0') == 0:
    num1 = int(nums[0])
    num2 = int(nums[1])
elif nums.count('0') == 1:
    if nums.index('0') == 1:
        num1 = int(nums[:2])
        num2 = int(nums[2])
    else:
        num1 = int(nums[0])
        num2 = int(nums[1:])
else:
    num1 = num2 = 10

print(num1 + num2)
