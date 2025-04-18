import sys
from decimal import Decimal, ROUND_HALF_UP

total = 0
total_grade = 0

grade_dict = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, "B-": 2.7,
              "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}

n = int(sys.stdin.readline())

for i in range(n):
    subject_info = sys.stdin.readline().strip().split()
    total_grade += int(subject_info[1])

    total += int(subject_info[1]) * grade_dict[subject_info[2]]

result = Decimal(str(total / total_grade)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"{result:.2f}")
