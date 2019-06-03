import sys

class myqueue():

    def __init__(self):
        self.queue = list()
        self.count = 0

    def push(self, num):
        self.queue.append(num)
        self.count += 1
    
    def pop(self):
        if self.count == 0:
            return -1
        else:
            self.count -= 1
            return self.queue.pop(0)

    def size(self):
        return self.count

    def empty(self):
        if self.count == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.queue[self.count-1]


if __name__ == "__main__":
    command_num = int(sys.stdin.readline())

    myqueue = myqueue()

    for _ in range(command_num):
        command = sys.stdin.readline().strip().split(" ")

        cmd = command[0]

        if cmd == "push":
            myqueue.push(command[1])
        elif cmd == "pop":
            print(myqueue.pop())
        elif cmd == "size":
            print(myqueue.size())
        elif cmd == "empty":
            print(myqueue.empty())
        elif cmd == "front":
            print(myqueue.front())
        elif cmd == "back":
            print(myqueue.back())

