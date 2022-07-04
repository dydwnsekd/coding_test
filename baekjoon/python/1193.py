n = int(input())
fraction_num = 0
counter = 1

while True:
    if fraction_num == n:
        print(f"{counter-1}/{counter-1}")
        break
    if fraction_num > n:
        print(fraction_num)
        print(counter)
        print(f"{n%(fraction_num-counter)}/{counter-1}")
        break
    else:
        fraction_num += counter
        counter += 1
