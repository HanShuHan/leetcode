from collections import deque


class RecentCounter(object):

    def __init__(self):
        self.arr = deque()

    def ping(self, t):
        self.arr.append(t)

        while self.arr and self.arr[0] < t - 3000:
            self.arr.popleft()

        return len(self.arr)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
