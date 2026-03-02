# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderIndex={n:i for i,n in enumerate(inorder)}
        def build(preL,preR,inL,inR):
            if preL>preR or inL>inR:
                return None
            root_val=preorder[preL]
            root=TreeNode(root_val)
            in_index=inOrderIndex[root_val]
            left_size=in_index-inL
            root.left=build(preL+1,preL+left_size,inL,in_index-1)
            root.right=build(preL+left_size+1,preR,in_index+1,inR)
            return root
        return build(0,len(preorder)-1,0,len(inorder))