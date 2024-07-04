from collections import deque


class RecentCounter:

    def __init__(self):
        self.__myQueue = deque()
        self.__counter = 0

    def ping(self, t: int) -> int:
        self.__myQueue.append(t)
        self.__counter += 1

        upper = t - 3000
        while self.__myQueue[0] < upper:
            self.__myQueue.popleft()
            self.__counter -= 1

        return self.__counter

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
