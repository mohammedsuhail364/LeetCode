# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def correctBstUtil(root,index):
            if not root:
                return 
            correctBstUtil(root.left,index)
            root.val=self.li[index[0]]
            index[0]+=1
            correctBstUtil(root.right,index)
        # your code here
        self.li=[]
        def dfs(node):
            if node:
                dfs(node.left)
                self.li.append(node.val)
                dfs(node.right)
        dfs(root)
        self.li.sort()
        index=[0]
        correctBstUtil(root,index)
        return root
        