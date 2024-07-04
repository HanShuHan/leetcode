class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        end_idx = min(len1, len2)
        result = []

        for i in range(end_idx):
            result.append(word1[i])
            result.append(word2[i])
        if len1 > end_idx:
            result.append(word1[end_idx:])
        elif len2 > end_idx:
            result.append(word2[end_idx:])

        return ''.join(result)
