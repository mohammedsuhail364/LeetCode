# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res=[]
        def dfs(node):
            if node:
                dfs(node.left)
                self.res.append(node.val)
                dfs(node.right)
        dfs(root)
        for i in range(1,len(self.res)):
            if self.res[i-1]>=self.res[i]:
                return False
        return True