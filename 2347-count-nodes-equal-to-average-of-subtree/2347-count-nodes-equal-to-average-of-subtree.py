# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.cnt=0
        def dfs(root):
            if not root:
                return [0,0]
            c1,v1=dfs(root.left)
            c2,v2=dfs(root.right)
            total=v1+v2+root.val
            cnt=c1+c2+1
            if (total//cnt)==root.val:
                self.cnt+=1
            return [cnt,total]
        dfs(root)
        return self.cnt
                