# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        nums = []
        max_sum = 0
        curr_odd = head

        while curr_odd:
            curr_even = curr_odd.next
            nums.append(curr_odd.val)
            nums.append(curr_even.val)

            curr_odd = curr_even.next

        nums_len = len(nums)
        for i in range(nums_len // 2):
            max_sum = max(nums[i] + nums[nums_len - 1 - i], max_sum)

        return max_sum
