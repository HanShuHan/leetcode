import heapq


class SmallestInfiniteSet(object):

    def __init__(self):
        self._curr_num = 1
        self._smallest_list = []

    def popSmallest(self):
        if not self._smallest_list:
            self._curr_num += 1
            return self._curr_num - 1
        return heapq.heappop(self._smallest_list)

    def addBack(self, num):
        if num < self._curr_num and num not in self._smallest_list:
            heapq.heappush(self._smallest_list, num)
