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
            temp=node.val+left+right
            res=max(res,temp)
            return node.val+max(left,right)

        dfs(root)
        return res