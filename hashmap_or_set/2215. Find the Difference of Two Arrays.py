class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1, s2 = set(nums1), set(nums2)
        l1, l2 = list(s1 - s2), list(s2 - s1)

        return [l1, l2]