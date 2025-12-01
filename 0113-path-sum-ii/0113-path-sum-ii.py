# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res=[]
        def dfs(node,path,targetSum):
            if not node:
                return
            path.append(node.val)
            targetSum-=node.val
            if not node.left and not node.right:
                if targetSum==0:
                    self.res.append(path[:])
            dfs(node.left,path,targetSum)
            dfs(node.right,path,targetSum)
            path.pop()
            return 
        dfs(root,[],targetSum)
        return self.res