import sys

quiz_count = 0
answer_count = []

n, d = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    collect_answer = int(sys.stdin.readline())
    quiz_count += collect_answer
    answer_count.append(collect_answer)

quiz_value = d // quiz_count

for i in range(n):
    print(quiz_value * answer_count[i])
