def get_divisor(num):

    divisor_list = []
    if num == 2:
        return [1, 2]
    elif num == 3:
        return [1, 3]

    for i in range(1, num//2 + 1):
        if num % i == 0:
            divisor_list.append(i)
            divisor_list.append(num // i)

    divisor_list = list(set(divisor_list))
    divisor_list.sort()
    return divisor_list


if __name__ == "__main__":
    print(get_divisor(2))
    print(get_divisor(3))
    print(get_divisor(4))
    print(get_divisor(10))
    print(get_divisor(30))
    print(get_divisor(49))
