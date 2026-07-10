# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder)


    def dfs(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)

        root.left = self.dfs(preorder[1:1+len(inorder[:idx])], inorder[:idx])
        root.right = self.dfs(preorder[1+len(inorder[:idx]):], inorder[idx+1:])

        return root