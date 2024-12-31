# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur=root
        while cur:
            if cur.val<val:
                if cur.right is None:
                    cur.right=TreeNode(val)
                    return root
                else:
                    cur=cur.right
            elif cur.val>val:
                if cur.left is None:
                    cur.left=TreeNode(val)
                    return root
                else:
                    cur=cur.left
        