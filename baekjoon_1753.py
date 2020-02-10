#-*- coning: utf-8 -*-

#https://www.acmicpc.net/problem/1753

'''

문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

예제 입력 1 
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
예제 출력 1 
0
2
3
7
INF

'''
class short_path(object):

    def __init__(self, v, e, line):
        self.v = v
        self.e = e
        self.line = line
        self.path_dict = dict()
        
        self.path_list = [999 for rows in range(v)]
        self.path_list[line] = 0


    def input_line (self, start_point, end_point, weight):
        key = '%s_%s' % (start_point, end_point)

        if start_point == self.line and self.path_list[start_point] > weight:
            self.path_list[start_point-1] = weight
    
        for i in range(self.v):
            if (self.path_list[start_point] != 999) and (self.path_list[end_point] > self.path_list[start_point] + weight):
                self.path_list[end_point] = self.path_list[start_point] + weight

    def print_path(self, line):

        for i in range(self.v):
            if self.path_list[i] == 999:
                self.path_list[i] = 'INF'
            
            print (self.path_list[i])


if __name__ == "__main__":
    
    v, e = input().split()
    line = input()
    v = int(v)
    e = int(e)
    line = int(line)-1
    
    shortpath = short_path(v, e, line)

    for i in range(e):
        start_point, end_point, weight = input().split()
        shortpath.input_line(int(start_point)-1, int(end_point)-1, int(weight))
        
    shortpath.print_path(line-1)
    

    