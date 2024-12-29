class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        if m == 0:
            return n

        if n == 0:
            return m

        if m == n == 1:
            return 1

        # 0   1, 2, 3, 4, 5, 6
        #   |-----------------
        # 1 | 0, 1, 2, 3, 4, 5
        # 2 | 1,

        count = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(1, n + 1):
            count[0][j] = j
        for i in range(1, m + 1):
            count[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    count[i][j] = count[i - 1][j - 1]
                else:
                    count[i][j] = min(count[i - 1][j - 1], count[i][j - 1], count[i - 1][j]) + 1

        return count[-1][-1]