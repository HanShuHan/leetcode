class Solution(object):
    def productExceptSelf(self, nums):
        total_product = 1
        total_zero = 0
        first_zero_index = -1
        size = len(nums)
        ans = []

        for i, num in enumerate(nums):
            if num != 0:
                total_product *= num
            else:
                total_zero += 1
                if first_zero_index == -1:
                    first_zero_index = i

        if total_zero > 1:
            ans = [0] * size
        elif total_zero == 1:
            ans = [0] * size
            print(first_zero_index)
            ans[first_zero_index] = total_product
        else:
            for num in nums:
                ans.append(total_product // num)

        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 0, 3]))
