# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root

        self.dfs(root)

        return root


    def dfs(self, root):
        if not root or (not root.left and not root.right):
            return 

        self.dfs(root.left)
        self.dfs(root.right)
        left = root.left if root.left else None
        right = root.right if root.right else None

        root.left = right
        root.right = left