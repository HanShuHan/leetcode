class Solution(object):
    def letterCombinations(self, digits):
        # Map of digits to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        # If the input is empty, return an empty list
        if not digits:
            return []

        # Result list to store the combinations
        result = []

        # Backtracking function
        def backtrack(index, path):
            # If the combination is complete, add it to the result
            if index == len(digits):
                result.append("".join(path))
                return

            # Get the letters for the current digit
            letters = phone_map[digits[index]]
            for letter in letters:
                # Add the letter to the current path
                path.append(letter)
                # Move to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the last letter
                path.pop()

        # Start the backtracking
        backtrack(0, [])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("234"))