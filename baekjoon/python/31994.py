import sys

seminar_dict = {}

for i in range(7):
    k, v = sys.stdin.readline().strip().split()
    seminar_dict[k] = int(v)


sorted_dict = sorted(seminar_dict, key=lambda x: seminar_dict[x], reverse=True)

print(sorted_dict[0])
