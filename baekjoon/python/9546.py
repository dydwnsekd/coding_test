import sys

n = int(sys.stdin.readline())

for _ in range(n):
    person_count = 0
    stop_count = int(sys.stdin.readline())

    for _ in range(stop_count):
        person_count = (person_count + 0.5) * 2
    print(int(person_count))
