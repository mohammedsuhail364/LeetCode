# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        q=deque([(root,"")])
        res=[]
        while q:
            for i in range(len(q)):
                node,val=q.popleft()
                new_val=val+str(node.val)+"->"
                if not node.left and not node.right:
                    res.append(new_val)
                if node.right:
                    q.append((node.right,new_val))
                if node.left:
                    q.append((node.left,new_val))
        final_res=[]
        for x in res:
            temp=x[:-2]
            final_res.append(temp)
        return final_res