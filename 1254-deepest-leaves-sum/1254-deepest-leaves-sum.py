# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        all_level=[]
        q=deque([root])
        while q:
            level=0
            for _ in range(len(q)):
                node=q.popleft()
                level+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            all_level.append(level)
        return all_level[-1]

