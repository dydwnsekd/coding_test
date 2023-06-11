import sys

money_dict = {"Franklin": 100, "Grant": 50, "Jackson": 20, "Hamilton": 10, "Lincoln": 5, "Washington": 1}
cases = int(sys.stdin.readline())

for _ in range(cases):
    total_money = 0
    wallet = list(sys.stdin.readline().split())
    for w in wallet:
        total_money += money_dict[w]

    print(f"${total_money}")
