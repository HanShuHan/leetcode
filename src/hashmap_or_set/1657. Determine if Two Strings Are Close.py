from collections import defaultdict


class Solution(object):
    def closeStrings(self, word1, word2):
        w1_len, w2_len = len(word1), len(word2)

        if w1_len != w2_len:
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for w1 in word1:
            d1[w1] += 1
        for w2 in word2:
            d2[w2] += 1

        if set(d1.keys()) != set(d2.keys()):
            return False

        if sorted(list(d1.values())) == sorted(list(d2.values())):
            return True

        return False
