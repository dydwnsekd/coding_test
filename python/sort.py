class sort(object):
    def __init__(self):
        pass

    def bubble(self, sort_list):
        for i in range(len(sort_list)-1, 0, -1):
            for j in range(0, i):
                if sort_list[j] > sort_list[j+1]:
                    sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
        return sort_list

    def selection(self, sort_list):
        for i in range(0, len(sort_list)):
            idx = i
            for j in range(i+1, len(sort_list)):
                if sort_list[idx] > sort_list[j]: idx=j
            sort_list[i], sort_list[idx] = sort_list[idx], sort_list[i]
            
        return sort_list

    def insertion(self, sort_list):
        for i in range(1, len(sort_list)):
            idx = i

            for j in range(i-1, -1, -1):
                if sort_list[idx] < sort_list[j]:
                    sort_list[idx], sort_list[j] = sort_list[j], sort_list[idx]
                    idx = j
                else:
                    break
        return sort_list