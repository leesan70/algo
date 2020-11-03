# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        unsorted_head, head.next = head.next, None

        while unsorted_head is not None:
            inserted = False
            to_sort = unsorted_head
            unsorted_head, sorted_head = unsorted_head.next, ListNode(next=head)
            prev, curr = sorted_head, head

            while curr is not None:
                if to_sort.val < curr.val:
                    prev.next, to_sort.next = to_sort, curr
                    inserted = True
                    break
                prev, curr = curr, curr.next

            if not inserted:
                prev.next, to_sort.next = to_sort, None

            head = sorted_head.next
        return head
