import sys

peper_dict = {"Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero": 125000}

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    result += peper_dict[sys.stdin.readline().strip()]

print(result)
