# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = None
        self.count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root, k)

        return self.ans

    def dfs(self, root, k):
        if not root:
            return 

        self.dfs(root.left, k)
        
        self.count += 1
        if k == self.count:
            self.ans = root.val
            return

        self.dfs(root.right, k)
        