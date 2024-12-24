class Solution(object):

    def __init__(self):
        self.result = []

    def letterCombinations(self, digits):
        digits_len = len(digits)

        if digits_len == 0:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        combination = []

        def dfs(index, _combination):
            if index == digits_len:
                self.result.append(''.join(_combination))
                return

            letters = mapping[digits[index]]
            for letter in letters:
                combination.append(letter)
                dfs(index + 1, combination)
                combination.pop()

        dfs(0, combination)

        return self.result
