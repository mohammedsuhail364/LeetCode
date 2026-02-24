# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(node,cur):
            if not node:
                return 0
            cur=cur*2+node.val
            if not node.right and not node.left:
                return cur
                
            return dfs(node.left,cur)+dfs(node.right,cur)
            
        return dfs(root,0)