# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Merge two sorted linked list
    def merge(self, h1: ListNode, h2: ListNode) -> ListNode:
        tmp_head = ListNode()
        head = ListNode()
        tmp_head.next = head

        while h1 is not None and h2 is not None:
            if h1.val <= h2.val:
                head.next = h1
                tmp = h1.next
                h1.next = None
                h1 = tmp
            else:
                head.next = h2
                tmp = h2.next
                h2.next = None
                h2 = tmp
            head = head.next
        if h1 is not None:
            head.next = h1
        elif h2 is not None:
            head.next = h2
        return tmp_head.next.next

    def divide(self, head: ListNode) -> List[ListNode]:
        count = self.count(head)
        first = head
        second = None
        tmp = head
        i = 0
        while i < count // 2:
            if i == count // 2 - 1:
                second = tmp.next
                tmp.next = None
            else:
                tmp = tmp.next
            i += 1
        return [first, second]

    def count(self, head: ListNode) -> int:
        count = 0
        tmp = head
        while tmp is not None:
            count += 1
            tmp = tmp.next
        return count

    def sortList(self, head: ListNode) -> ListNode:
        if self.count(head) > 1:
            l, r = self.divide(head)
            l = self.sortList(l)
            r = self.sortList(r)
            return self.merge(l, r)
        return head
