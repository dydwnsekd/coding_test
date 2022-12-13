def get_fibonacci_num(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return get_fibonacci_num(num - 1) + get_fibonacci_num(num - 2)


def get_fibonacci_list(num):
    fibonacci_list = [0, 1, 1]

    for i in range(3, num+1):
        fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])

    return fibonacci_list


if __name__ == "__main__":
    for i in range(10):
        print(i, get_fibonacci_num(i))

    print(get_fibonacci_list(10))

