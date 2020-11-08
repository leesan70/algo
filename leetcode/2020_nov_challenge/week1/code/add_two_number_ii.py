# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNumber(l: ListNode) -> int:
            num = 0
            while l is not None:
                num = 10 * num + l.val
                l = l.next
            return num

        added = getNumber(l1) + getNumber(l2)
        result = None

        while added > 0:
            new_head = ListNode(added % 10, result)
            result = new_head
            added = added // 10
        return result if result is not None else ListNode()
