import sys

score_dict = {"miss": 0, "bad": 200, "cool": 400, "great": 600, "perfect": 1000}

lv, grade = sys.stdin.readline().strip().split()
lv = int(lv)

print(lv * score_dict[grade])
