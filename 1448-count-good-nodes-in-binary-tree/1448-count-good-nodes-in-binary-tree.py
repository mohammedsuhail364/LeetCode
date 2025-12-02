# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,cur_max):
            if not node:
                return 0
            count =1 if cur_max<=node.val else 0
            cur_max=max(cur_max,node.val)
            left =dfs(node.left,cur_max)
            right=dfs(node.right,cur_max)
            count += (left + right)
            return count
        return dfs(root,root.val)
            