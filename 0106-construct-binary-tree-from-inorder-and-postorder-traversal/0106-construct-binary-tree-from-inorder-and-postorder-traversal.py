# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inOrderIndex={n:i for i,n in enumerate(inorder)}
        def build(inL,inR,posL,posR):
            if inL>inR or posL>posR:
                return None
            root_val=postorder[posR]
            root=TreeNode(root_val)
            in_index=inOrderIndex[root_val]
            left_size=in_index-inL
            root.left=build(inL,in_index-1,posL,posL+left_size-1)
            root.right=build(in_index+1,inR,posL+left_size,posR-1)
            return root
        return build(0,len(inorder)-1,0,len(postorder)-1)