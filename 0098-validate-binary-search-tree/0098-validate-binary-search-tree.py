# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q=deque([(float('-inf'),root,float('inf'))])
        while q:
            for i in range(len(q)):
                min_val,node,max_val=q.popleft()
                if not min_val<node.val<max_val:
                    return False
                if node.left:
                    q.append((min_val,node.left,node.val))
                if node.right:
                    q.append((node.val,node.right,max_val))
        return True
