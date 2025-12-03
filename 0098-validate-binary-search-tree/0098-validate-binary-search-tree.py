# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,left_max,right_max):
            if not node:
                return True
            if node.val<left_max or node.val>right_max:
                return False
            left = validate(node.left,left_max,node.val)
            right = validate(node.right,node.val,right_max)
            return left and right
        return validate(root,-inf,inf)
            
            
        