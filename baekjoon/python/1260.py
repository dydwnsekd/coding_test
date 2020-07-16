import sys

class stack():

    s = list()
    index = 0

    def push(self, num):
        self.s.append(num)
        self.index += 1
    
    def pop(self):
        self.index -= 1
        return self.s.pop()

    def stack_len(self):
        return self.index

n, m, v = map(int, sys.stdin.readline().split(" "))

path_list = [[] for _ in range(n+1)]

for i in range(m):
    start_point, end_point = map(int, sys.stdin.readline().split(" "))
    path_list[start_point].append(end_point)
    path_list[end_point].append(start_point)

for i in range(n+1):
    path_list[i].sort()

# BFS
bfs_list = [v]
bfs_list.extend(path_list[v])

for i in bfs_list:
    for j in path_list[i]:
        if j not in bfs_list:
            bfs_list.append(j)


# DFS
dfs_list = [v]
mystack = stack()

while(len(path_list[v]) > 0):
    mystack.push(path_list[v].pop())

while(mystack.stack_len() > 0):
    i = mystack.pop()
    if i not in dfs_list:
        dfs_list.append(i)
        while(len(path_list[i]) > 0):
            mystack.push(path_list[i].pop())

    else:
        continue

for i in dfs_list:
    print(i, end=" ")

print()
for i in bfs_list:
    print(i, end=" ")

