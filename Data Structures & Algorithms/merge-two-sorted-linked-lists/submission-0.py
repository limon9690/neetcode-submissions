# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        if not list1:
            return list2

        if not list2:
            return list1

        dummy = ListNode(-1)
        curr = dummy
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next

            curr = curr.next
        
        if p1:
            curr.next = p1

        if p2:
            curr.next = p2

        return dummy.next