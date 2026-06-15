# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        sec_head = slow.next
        slow.next = None

        sec_head = self.reverse(sec_head)
        p1 = head
        p2 = sec_head
        
        while p1 and p2:
            p1_nxt = p1.next
            p2_nxt = p2.next

            p1.next = p2
            p2.next = p1_nxt
            
            p1 = p1_nxt
            p2 = p2_nxt

        return


    def reverse(self, node):
        prev = None
        curr = node

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev