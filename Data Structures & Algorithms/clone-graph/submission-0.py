"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}
        visited = set()

        def populate_map(nde):
            if not nde:
                return 

            visited.add(nde.val)
            node_map[nde.val] = Node(nde.val)

            for nei in nde.neighbors:
                if nei.val not in visited:
                    populate_map(nei)


        populate_map(node)
        visited.clear()

        def clone(nde):
            if not nde:
                return 

            visited.add(nde.val)
            clone_nde = node_map[nde.val]

            for nei in nde.neighbors:
                    clone_nei = node_map[nei.val]
                    clone_nde.neighbors.append(clone_nei)

                    if nei.val not in visited:
                        clone(nei)

        
        clone(node)
        return node_map[node.val] if node else None

        