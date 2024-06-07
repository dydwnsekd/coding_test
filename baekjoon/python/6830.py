import sys

result = ""
min_temp = 200

while True:
    city, temperature = sys.stdin.readline().strip().split()

    temperature = int(temperature)

    if min_temp > temperature:
        min_temp = temperature
        result = city

    if city == "Waterloo":
        break

print(result)

