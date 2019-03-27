import sys
import heapq

class short_path(object):

    def __init__(self, v, e, line):
        self.v = v
        self.e = e
        self.line = line
        self.path_list = [[] for _ in range(self.v)]

    def input_line (self, start_point, end_point, weight):
        self.path_list[start_point].append([weight, end_point])
                

    def find_path(self):
        pq = []
        dist = [987654321] * self.v
        dist[self.line] = 0
        heapq.heappush(pq, (0, self.line))

        while pq:
            start_weight, start_point = heapq.heappop(pq)
            if dist[start_point] < start_weight:
                continue
            
            for end_weight, end_point in self.path_list[start_point]:
                end_weight += start_weight
                if dist[end_point] > end_weight:
                    dist[end_point] = end_weight
                    heapq.heappush(pq, [end_weight, end_point])

        return dist

if __name__ == "__main__":
    v, e = sys.stdin.readline().split()
    
    line = int(sys.stdin.readline()) - 1
    v = int(v)
    e = int(e)
    
    shortpath = short_path(v, e, line)

    for i in range(e):
        start_point, end_point, weight = sys.stdin.readline().split()
        shortpath.input_line(int(start_point)-1, int(end_point)-1, int(weight))

    result = shortpath.find_path()

    for i in range(len(result)):
        if result[i] != 987654321:
            print (result[i])
        else:
            print ('INF')
        