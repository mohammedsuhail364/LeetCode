# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderIndexMap={n:i for i,n in enumerate(inorder)}
        def dfs(preL,preR,inL,inR):
            if preL>preR or inL>inR:
                return None
            root_val=preorder[preL]
            inIndex=inOrderIndexMap[root_val]
            left_size=inIndex-inL
            root=TreeNode(root_val)
            root.left=dfs(preL+1,preL+left_size,inL,inIndex-1)
            root.right=dfs(preL+left_size+1,preR,inIndex+1,inR)
            return root
        return dfs(0,len(preorder)-1,0,len(inorder)-1)