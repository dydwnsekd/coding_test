import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    school_dict = {}

    for _ in range(n):
        school, alchol = sys.stdin.readline().strip().split()
        alchol = int(alchol)
        school_dict[school] = alchol

    sorted_school = sorted(school_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_school[0][0])

