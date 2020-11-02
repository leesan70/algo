# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        dec = 0
        while head is not None:
            # Bitwise manipulation equivalent of 2 * dec + head.val
            dec = dec << 1 | head.val
            head = head.next
        return dec
