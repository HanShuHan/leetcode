# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None

        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next

        return head
