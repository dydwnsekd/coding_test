import sys


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
        return [self.calculate(i) % 1000000 for i in range(n + 1)]


fibonacci = Fibonacci()

num = int(sys.stdin.readline())

print(fibonacci.get_fibonacci_list(num)[num])


