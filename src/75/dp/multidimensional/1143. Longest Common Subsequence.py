class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        txt1_len = len(text1)
        txt2_len = len(text2)

        if txt1_len == txt2_len == 1:
            return int(text1[0] == text2[0])

        count = [[0] * (txt2_len + 1) for _ in range(txt1_len + 1)]

        for i in range(1, txt1_len + 1):
            for j in range(1, txt2_len + 1):
                if text1[i - 1] == text2[j - 1]:
                    count[i][j] = count[i - 1][j - 1] + 1
                else:
                    count[i][j] = max(count[i - 1][j], count[i][j - 1])

        return count[-1][-1]
