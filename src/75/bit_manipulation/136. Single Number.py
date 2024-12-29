class Solution(object):
    # def singleNumber(self, nums):
    #     if len(nums) == 1:
    #         return nums[0]
    #
    #     count = Counter(nums)
    #
    #     for k , v in count.items():
    #         if v == 1:
    #             return k

    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]

        # 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1
        # 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1
        # 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1

        result = 0

        for num in nums:
            result ^= num

        return result
