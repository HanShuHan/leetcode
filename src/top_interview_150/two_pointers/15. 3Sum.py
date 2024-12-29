class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        left, right = 0, len(nums) - 1
        result_set = set()

        while left + 1 < right:
            inner_left, inner_right = left + 1, right - 1
            sum_of_sides = nums[left] + nums[right]

            while inner_left <= inner_right:
                mid = (inner_left + inner_right) // 2
                sum_of_triplet = sum_of_sides + nums[mid]

                if sum_of_triplet == 0:
                    result_set.add(tuple(sorted([nums[left], nums[right], nums[mid]])))
                    break
                elif sum_of_triplet < 0:
                    inner_left = mid + 1
                else:
                    inner_right = mid - 1

            if sum_of_sides + nums[left + 1] >= 0:
                right -= 1
            else:
                left += 1

        return list(list(triplet) for triplet in result_set)


if __name__ == '__main__':
    s = Solution()
    s.threeSum([-1, 0, 1, 2, -1, -4])
