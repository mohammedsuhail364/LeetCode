# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=-inf
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            curr=left+right+node.val
            res=max(res,curr)
            return max(left,right)+node.val
        dfs(root)
        return res