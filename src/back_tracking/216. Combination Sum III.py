class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def backtrack(index, digits, path):
            nums_size = len(digits)

            if nums_size < k - index:
                return

            if index == k:
                if sum(path) == n:
                    result.append(path[:])
                return

            for i in range(nums_size):
                path.append(digits[i])
                backtrack(index + 1, digits[i + 1:], path)
                path.pop()

        backtrack(0, [i for i in range(1, 10)], [])

        return result
