import sys

result = 0
price_dict = {"Paper": 57.99, "Printer": 120.50, "Planners": 31.25, "Binders": 22.50, "Calendar": 10.95,
              "Notebooks": 11.20, "Ink": 66.95}

while True:
    item = sys.stdin.readline().strip()

    if item == "EOI":
        break

    result += price_dict[item]

print(f"${result}")

