class Solution(object):
    def isSubsequence(self, s, t):
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True

        if s_len > t_len:
            return False

        i, j = 0, 0

        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == s_len
