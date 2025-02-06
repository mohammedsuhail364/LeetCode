# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx=0
        inorder_map={}
        for i,j in enumerate(inorder):
            inorder_map[j]=i
        def helper(left,right):
            if left>right:
                return None
            root_val=preorder[self.pre_idx]
            root=TreeNode(root_val)
            
            self.pre_idx+=1
            root.left=helper(left,inorder_map[root_val]-1)
            root.right=helper(inorder_map[root_val]+1,right)
            return root
            
            
        return helper(0,len(inorder)-1)