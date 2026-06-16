# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None

        length = self.find_length(head)

        if length == n:
            return head.next

        curr = head

        for i in range(length-n-1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head


    def find_length(self, head):
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        return length