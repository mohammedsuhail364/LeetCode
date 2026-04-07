# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # refer neetcode
        def dfs(node):
            if not node:
                return [0,0] # [withRoot,withOutRoot]
            left=dfs(node.left)
            right=dfs(node.right)
            withRoot=node.val+left[1]+right[1] # we can take the withOutRoot Value why because we cannot choose the child value that is the reason
            withOutRoot=max(left)+max(right) # we can choose the max value because we can skip the root so we can pick the child also so no restrictions 
            return [withRoot,withOutRoot]
        return max(dfs(root))