class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        num_of_zero = 0
        firs_zero_index = -1
        size_of_nums = len(nums)
        result = [0] * size_of_nums

        for i in range(size_of_nums):
            if nums[i] != 0:
                product *= nums[i]
            else:
                num_of_zero += 1
                if firs_zero_index == -1:
                    firs_zero_index = i

        if num_of_zero == 1:
            result[firs_zero_index] = product
        elif num_of_zero == 0:
            for i in range(size_of_nums):
                result[i] = product // nums[i]

        return result
