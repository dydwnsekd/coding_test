import sys

case_count = int(sys.stdin.readline().split()[0])

for _ in range(case_count):
    case_list = list(map(int, sys.stdin.readline().split(" ")))

    student_count = case_list[0]
    student_average = sum(case_list[1:])/student_count

    count = 0

    for i in case_list[1:]:
        if(student_average < i):
            count += 1

    print ("%0.3f%s" % (round((count/student_count) * 100, 3), "%"))
