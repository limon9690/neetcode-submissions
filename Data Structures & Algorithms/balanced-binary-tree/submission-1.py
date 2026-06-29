# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.dfs(root)

        return False if res == -1 else True


    def dfs(self, root):
        if not root:
            return 0

        lh = self.dfs(root.left)
        rh = self.dfs(root.right)

        if lh == -1 or rh == -1:
            return -1

        if abs(lh-rh) > 1:
            return -1

        return 1 + max(lh, rh)