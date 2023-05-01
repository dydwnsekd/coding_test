import sys

human_list1 = []
human_list2 = []
partner_dict1 = {}
partner_dict2 = {}

cases = int(sys.stdin.readline())

human_list1 = sys.stdin.readline().strip().split()
human_list2 = sys.stdin.readline().strip().split()
flag = True

for i in range(cases):
    partner_dict1[human_list1[i]] = human_list2[i]
    partner_dict2[human_list2[i]] = human_list1[i]

    if human_list1[i] == human_list2[i]:
        flag = False

if partner_dict1 == partner_dict2 and flag:
    print("good")
else:
    print("bad")
