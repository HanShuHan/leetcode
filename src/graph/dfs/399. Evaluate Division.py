from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        # reciprocal, chain rules, self / self == 1, variable does not exist
        formula = defaultdict(dict)
        result = []

        for (a, b), val in zip(equations, values):
            formula[a][b] = val
            formula[b][a] = 1 / val

        def dfs(a, b, visited):
            if a not in formula or b not in formula:
                return -1.0

            if a == b:
                return 1.0

            visited.add(a)
            for k, v in formula[a].items():
                if k == b:
                    return v
                elif k not in visited:
                    res = dfs(k, b, visited)

                    if res != -1.0:
                        return v * res

            return -1.0

        for a, b in queries:
            result.append(dfs(a, b, set()))

        return result


if __name__ == '__main__':
    s = Solution()
    s.calcEquation([["a", "b"], ["b", "c"]],
                   [2.0, 3.0],
                   [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
