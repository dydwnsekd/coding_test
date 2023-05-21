import sys

grade_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
result_grade = 0
sum_grade = 0

for _ in range(20):
    subject, grade, grade_score = sys.stdin.readline().strip().split()
    grade = float(grade)

    if grade_score != "P":
        result_grade += grade * grade_dict[grade_score]
        sum_grade += grade

print(format(round(result_grade/sum_grade, 6), "0.6f"))
