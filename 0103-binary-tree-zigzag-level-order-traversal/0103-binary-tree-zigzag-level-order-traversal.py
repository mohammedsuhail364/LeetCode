# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        all_level=[]
        q=deque([(root)])
        flag=True
        while q:
            level=[]
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag:
                all_level.append(level)
                flag=False
            else:
                all_level.append(level[::-1])
                flag=True
            
        return all_level


