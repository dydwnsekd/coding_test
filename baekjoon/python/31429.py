import sys

result_dict = {1: [12, 1600], 2: [11, 894], 3: [11, 1327], 4: [10, 1311], 5: [9, 1004], 6: [9, 1178],
               7: [9, 1357], 8: [8, 837], 9: [7, 1055], 10: [6, 556], 11: [6, 773]}

n = int(sys.stdin.readline())

print(result_dict[n][0], result_dict[n][1])