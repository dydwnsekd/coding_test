def get_divisor(num):

    divisor_list = []
    for i in range(1, num//2):
        if num % i == 0:
            if i not in divisor_list:
                divisor_list.append(i)
                divisor_list.append(num // i)

    divisor_list.sort()
    return divisor_list


if __name__ == "__main__":
    print(get_divisor(10))
    print(get_divisor(30))
