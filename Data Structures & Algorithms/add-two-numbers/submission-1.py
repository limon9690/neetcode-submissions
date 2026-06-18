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

        while p1 or p2 or extra:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            total = v1 + v2 + extra
            extra = total // 10

            tail.next = ListNode(total % 10)
            tail = tail.next

            if p1:
                p1 = p1.next
            
            if p2:
                p2 = p2.next


        return dummy.next