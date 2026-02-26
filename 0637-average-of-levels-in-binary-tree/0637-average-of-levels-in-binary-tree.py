# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res=[]
        q=deque([(root)])
        while q:
            level=0
            n=0
            for _ in range(len(q)):
                node=q.popleft()
                level+=node.val
                n+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level/n)
        return res