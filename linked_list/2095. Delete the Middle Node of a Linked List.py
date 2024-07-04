from charset_normalizer.md import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0, head)
        slow = prev
        fast = prev

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return prev.next
