class Fibonacci:
    def __init__(self):
        self.fibonacci = {0: 0, 1: 1}

    def calculate(self, n):
        if n in self.fibonacci:
            return self.fibonacci[n]
        else:
            self.fibonacci[n] = self.calculate(n - 1) + self.calculate(n - 2)
            return self.fibonacci[n]

    def get_fibonacci_num(self, n):
        return self.calculate(n)

    def get_fibonacci_list(self, n):
        return [self.calculate(i) for i in range(n + 1)]


if __name__ == "__main__":
    fibonacci = Fibonacci()

    for i in range(10):
        print(i, fibonacci.get_fibonacci_num(i))

    print(fibonacci.get_fibonacci_list(10))
    print(fibonacci.get_fibonacci_num(100))

