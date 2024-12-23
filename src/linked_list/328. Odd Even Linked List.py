# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return None

        if head.next is None:
            return head

        odd, even = head, head.next
        curr_odd, curr_even = odd, even

        while curr_even and curr_even.next:
            curr_odd.next = curr_even.next
            curr_odd = curr_odd.next
            curr_even.next = curr_odd.next
            curr_even = curr_even.next

        curr_odd.next = even

        return odd
