class Solution(object):
    def mergeAlternately(self, word1, word2):
        w1_len, w2_len = len(word1), len(word2)
        min_len = min(w1_len, w2_len)
        result = ''

        for i in range(min_len):
            result += word1[i] + word2[i]

        if w1_len > min_len:
            result += word1[min_len:]
        elif w2_len > min_len:
            result += word2[min_len:]

        return result
