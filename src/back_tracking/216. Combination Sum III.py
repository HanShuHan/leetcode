class Solution(object):

    def __init__(self):
        self.result = []

    def combinationSum3(self, k, n):
        nums = [i for i in range(1, 10)]

        def dfs(index, _nums, total, _combination):
            if index == k:
                if sum(_combination) == n:
                    self.result.append(_combination[:])
                return

            for i in range(len(_nums)):
                curr_total = total + _nums[i]
                if (index == k - 1 and curr_total > n
                        or index < k - 1 and curr_total >= n):
                    break

                # 1, 2, 3, 4, 5, 6, 7, 8, 9
                _combination.append(_nums[i])
                dfs(index + 1, _nums[i + 1:], curr_total, _combination)
                _combination.pop()

        dfs(0, nums, 0, [])

        return self.result
