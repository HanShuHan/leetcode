class Solution(object):

    def findCircleNum(self, isConnected):
        n = len(isConnected)

        if n == 1:
            return 1

        visited_city = [0] * n
        provinces = 0

        def dfs(city):
            visited_city[city] = 1

            for j in range(n):
                if j != city and isConnected[city][j] and not visited_city[j]:
                    dfs(j)

        for i in range(n):
            if not visited_city[i]:
                dfs(i)
                provinces += 1

        return provinces
