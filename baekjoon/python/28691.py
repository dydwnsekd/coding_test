import sys

club_dict = {"M": "MatKor", "W": "WiCys", "C": "CyKor", "A": "AlKor", "$": "$clear"}

s = sys.stdin.readline().strip()
print(club_dict[s])
