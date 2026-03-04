# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_index={n:i for i, n in enumerate(postorder)}
        n=len(preorder)
        def dfs(preL,preR,posL,posR):
            if preL>preR:
                return None
            root_val=preorder[preL]
            root=TreeNode(root_val)
            if preL==preR:
                return root
            left_root=preorder[preL+1]
            index=post_index[left_root]
            left_size=index-posL+1
            root.left=dfs(preL+1,preL+left_size,posL,index)
            root.right=dfs(preL+left_size+1,preR,index+1,posR-1)
            return root
        return dfs(0,n-1,0,n-1)