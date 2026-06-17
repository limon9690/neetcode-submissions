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
        
        nodes_table = {}
        curr = head

        while curr:
            nodes_table[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        dummy = Node(-1)
        tail = dummy

        while curr:
            tail.next = nodes_table[curr]
            tail = tail.next
            tail.random = nodes_table[curr.random] if curr.random else None
            curr = curr.next


        return dummy.next