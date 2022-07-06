n = int(input())
fraction_num = 0
counter = 1

while True:
    prev_counter = counter - 1
    if fraction_num == n:
        print(f"{prev_counter}/{prev_counter}")
        break
    if fraction_num > n:
        print(fraction_num)
        print(counter)
        print(f"{n%(fraction_num-prev_counter)}/{prev_counter}")
        break
    else:
        fraction_num += counter
        counter += 1
