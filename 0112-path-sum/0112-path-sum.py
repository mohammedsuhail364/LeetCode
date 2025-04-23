# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q=deque([(root,0)])
        while q:
            for i in range(len(q)):
                node,val=q.popleft()
                if not node.left and not node.right and val+node.val==targetSum:
                    return True
                if node.left:
                    q.append((node.left,val+node.val))
                if node.right:
                    q.append((node.right,val+node.val))
        return False
        