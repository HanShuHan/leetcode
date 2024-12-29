# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        if head.next is None:
            return None

        # 0, 1, 2, 3, 4, 5, 6, 7
        curr = slow = fast = head

        while fast and fast.next:
            curr = slow
            slow = slow.next
            fast = fast.next.next

        curr.next = slow.next

        return head
