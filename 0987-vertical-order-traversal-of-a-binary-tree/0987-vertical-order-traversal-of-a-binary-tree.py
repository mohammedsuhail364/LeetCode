# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # as same as the normal vertical order but one difference is if the rows are different we cannot sort like the normal one
        res=defaultdict(list)
        q=deque([(root,0,0)]) # (node,row,col)
        final_res=[]
        while q:
            n=len(q)
            for _ in range(n):
                node,row,col=q.popleft()
                res[col].append((row,node.val))
                if node.left:
                    q.append((node.left,row+1,col-1))
                if node.right:
                    q.append((node.right,row+1,col+1))
        for col in sorted(res):
            rows=res[col]
            tmp=[val for row,val in sorted(rows)]
            final_res.append(tmp)
        return final_res
            