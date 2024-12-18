from collections import defaultdict


class Solution(object):

    def findCircleNum(self, isConnected):
        provinces = 0
        size = len(isConnected)
        cities_visited = [False] * size

        def dfs(city):
            cities_visited[city] = True

            for j in range(size):
                if j != city and isConnected[city][j] and not cities_visited[j]:
                    dfs(j)

        for i in range(size):
            if not cities_visited[i]:
                dfs(i)
                provinces += 1

        return provinces
