class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        digitToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if not digits:
            return result

        def crossCompose(composition: str, digits: str):
            if not digits:
                result.append(composition)
            else:
                letters = digitToLetters[digits[0]]
                for letter in letters:
                    crossCompose(composition + letter, digits[1:])

        crossCompose('', digits)

        return result