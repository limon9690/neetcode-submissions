# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height = [0]

        self.maxHeight(root, height)

        return height[0]


    def maxHeight(self, root, height):
        if not root:
            return 0

        lh = self.maxHeight(root.left, height)
        rh = self.maxHeight(root.right, height)
        height[0] = max(height[0], lh+rh)

        return 1 + max(lh, rh)