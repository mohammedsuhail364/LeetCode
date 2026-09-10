# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res=0
        def dfs(node):
            nonlocal res
            if not node:
                return [0,0]
            leftSum,leftTotalNodes=dfs(node.left)
            rightSum,rightTotalNodes=dfs(node.right)
            totalNode=1+leftTotalNodes+rightTotalNodes
            nodeSum = node.val + leftSum + rightSum
            res+=1 if floor(nodeSum/totalNode)==node.val else 0
            return [nodeSum,totalNode]
        dfs(root)
        return res



            
