class Solution(object):
    def maxVowels(self, s, k):
        vowels = set('aeiou')
        vowels_count = 0
        max_vowels_count = 0

        for i in range(0, k):
            if s[i] in vowels:
                vowels_count += 1
        max_vowels_count = vowels_count

        for i in range(k, len(s)):
            if s[i] in vowels:
                vowels_count += 1
            if s[i - k] in vowels:
                vowels_count -= 1
            max_vowels_count = max(max_vowels_count, vowels_count)

        return max_vowels_count