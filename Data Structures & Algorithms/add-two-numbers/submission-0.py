# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        p1 = l1
        p2 = l2
        extra = 0

        while p1 and p2:
            total = p1.val + p2.val + extra
            rem = total % 10
            res = total // 10
            tail.next = ListNode(rem)
            tail = tail.next
            extra = res
            p1 = p1.next
            p2 = p2.next

        while p1:
            total = p1.val + extra
            rem = total % 10
            res = total // 10
            tail.next = ListNode(rem)
            tail = tail.next
            extra = res
            p1 = p1.next

        while p2:
            total = p2.val + extra
            rem = total % 10
            res = total // 10
            tail.next = ListNode(rem)
            tail = tail.next
            extra = res
            p2 = p2.next

        if extra == 1:
            tail.next = ListNode(extra)
            tail = tail.next

        return dummy.next