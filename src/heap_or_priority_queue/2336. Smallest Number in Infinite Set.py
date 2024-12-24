import heapq


class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = []
        self.curr_num = 1

    def popSmallest(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            self.curr_num += 1
            return self.curr_num - 1

    def addBack(self, num):
        if num < self.curr_num and num not in self.heap:
            heapq.heappush(self.heap, num)
