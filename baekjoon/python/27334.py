import sys

n = int(sys.stdin.readline())
marathon_record = list(map(int, sys.stdin.readline().split()))

sorted_nums = sorted(set(marathon_record))
ranks = {}
rank = 1
for num in sorted_nums:
    ranks[num] = rank
    rank += marathon_record.count(num)
marathon_rank = [ranks[record] for record in marathon_record]

for rank in marathon_rank:
    print(rank)

