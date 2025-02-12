# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.li=[]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if root:
                dfs(root.left)
                self.li.append(root.val)
                dfs(root.right)
        dfs(root)
        return self.li[k-1]
        