# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res=0
        q=deque([(root,"")])
        while q:
            for i in range(len(q)):
                node,val=q.popleft()
                if not node.right and not node.left:
                    
                    self.res+=int(val+str(node.val))
                if node.left:
                    q.append((node.left,val+str(node.val)))
                if node.right:
                    q.append((node.right,val+str(node.val)))
        return self.res