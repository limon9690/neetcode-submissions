# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        self.dfs(root, float('-inf'), count)

        return count[0]

    def dfs(self, root, largest, count):
        if not root:
            return

        if root.val >= largest:
            count[0] += 1

        largest = max(largest, root.val)

        self.dfs(root.left, largest, count)
        self.dfs(root.right, largest, count)