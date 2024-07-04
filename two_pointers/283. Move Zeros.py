class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        lastIdx = self.lastIndexOfNonZero(nums)

        i = 0
        for count in range(lastIdx + 1):
            if nums[i] == 0:
                zero = nums.pop(i)
                nums.append(zero)
            else:
                i += 1

    def lastIndexOfNonZero(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                return i
        return -1
