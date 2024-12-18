from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0

            visited.add(a)
            for bb, val in graph[a].items():
                if bb == b:
                    return val
                elif bb not in visited:
                    res = dfs(bb, b, visited)
                    if res != -1.0:
                        return val * res

            return -1.0

        result = []

        for a, b in queries:
            result.append(dfs(a, b, set()))

        return result
