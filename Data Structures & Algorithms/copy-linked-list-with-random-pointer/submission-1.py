"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head

        while curr:
            nxt = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nxt
            curr = nxt
        
        dummy = head.next
        curr = head

        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        new_head = head.next
        curr = new_head

        while curr:
            nxt = curr.next.next if curr.next else None
            curr.next = nxt
            curr = nxt

        head.next = None
        return new_head