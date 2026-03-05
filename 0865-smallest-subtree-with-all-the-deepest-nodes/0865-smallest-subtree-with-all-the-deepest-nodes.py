# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # refer neetcode
        def dfs(node):
            if not node:
                return [0,None] # [height,Lowest common anchestor]
            left=dfs(node.left)
            right=dfs(node.right)
            if left[0]==right[0]: # if the height of left and right are same we can return the root why? because that would be the LCA
                return [left[0]+1,node]
            elif left[0]>right[0]:
                return [left[0]+1,left[1]]
            return [right[0]+1,right[1]]
        return dfs(root)[1] # LCA 