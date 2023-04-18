import sys

while True:
    text = sys.stdin.readline().strip().lower()

    if text == "eoi":
        break

    if "nemo" in text:
        print("Found")
    else:
        print("Missing")

