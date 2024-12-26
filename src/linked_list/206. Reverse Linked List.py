# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return None

        if head.next is None:
            return head

        # 1 -> 2 -> 3 -> 4 -> 5
        curr = head.next
        prev = head
        prev.next = None
        next = curr.next

        curr.next = prev

        while next:
            prev = curr
            curr = next
            next = curr.next
            curr.next = prev

        return curr
