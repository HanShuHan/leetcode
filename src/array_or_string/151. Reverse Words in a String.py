class Solution(object):
    def reverseWords(self, s):
        reversed_words = s.strip().split()[::-1]
        return ' '.join(reversed_words)
