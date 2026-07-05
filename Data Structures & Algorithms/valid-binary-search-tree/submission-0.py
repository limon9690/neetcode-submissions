# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, start, end):
        if not root:
            return True

        left = self.dfs(root.left, start, root.val)
        right = self.dfs(root.right, root.val, end)

        return left and right and (root.val > start and root.val < end)