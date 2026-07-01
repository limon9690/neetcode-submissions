# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)

    
    def dfs(self, root, subRoot):
        if not root:
            return False

        if root.val == subRoot.val:
            flag = self.isSameTree(root, subRoot)

            if flag:
                return True

        left = self.dfs(root.left, subRoot)
        right = self.dfs(root.right, subRoot)

        return left or right



    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right