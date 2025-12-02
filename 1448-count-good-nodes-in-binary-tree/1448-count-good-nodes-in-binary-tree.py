# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(node,cur_max):
            nonlocal res
            if not node:
                return
            if cur_max<=node.val:
                res+=1
            cur_max=max(cur_max,node.val)
            dfs(node.left,cur_max)
            dfs(node.right,cur_max)
        dfs(root,root.val)
        return res
            