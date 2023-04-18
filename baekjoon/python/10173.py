import sys

while True:
    text = sys.stdin.readline().strip()

    if text == "EOI":
        break

    text = text.lower()

    if "nemo" in text:
        print("Found")
    else:
        print("Missing")

