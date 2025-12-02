# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        temp=[]
        def dfs(node):
            if node:
                temp.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)

        root.left=None
        root.right=None
        res=root
        for n in temp[1:]:
            root.right=TreeNode(n)
            root=root.right
        return res
        