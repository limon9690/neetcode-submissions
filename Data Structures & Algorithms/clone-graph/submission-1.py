"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes_map = {}

        def dfs(nde):
            if nde.val in nodes_map:
                return nodes_map[nde.val]

            clone_nde = Node(nde.val)
            nodes_map[nde.val] = clone_nde

            for nei in nde.neighbors:
                clone_nde.neighbors.append(dfs(nei))


            return clone_nde

        return dfs(node) 

        