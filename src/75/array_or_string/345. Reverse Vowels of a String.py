class Solution(object):
    def reverseVowels(self, s):
        s_len = len(s)

        if s_len == 1:
            return s

        s_list = list(s)
        vowels = set('aeiouAEIOU')
        vowel_indices = []

        for i in range(s_len):
            if s[i] in vowels:
                vowel_indices.append(i)

        for j in range(len(vowel_indices) // 2):
            front, end = vowel_indices[j], vowel_indices[-1 - j]

            s_list[front], s_list[end] = s_list[end], s_list[front]

        return ''.join(s_list)
