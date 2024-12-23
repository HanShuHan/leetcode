from collections import deque


class Solution(object):
    def maxVowels(self, s, k):
        s_len = len(s)
        vowels = set('aeiou')

        if s_len == 1:
            return int(s in vowels)

        sliding_window = deque([])
        count = max_count = 0

        for i in range(k):
            is_vowel = int(s[i] in vowels)
            sliding_window.append(is_vowel)
            count += is_vowel

        max_count = count
        if max_count == k:
            return max_count

        for j in range(k, s_len):
            left_most = sliding_window.popleft()
            right_most = int(s[j] in vowels)

            sliding_window.append(right_most)
            count += (right_most - left_most)
            if count > max_count:
                max_count = count

            if max_count == k:
                break

        return max_count
