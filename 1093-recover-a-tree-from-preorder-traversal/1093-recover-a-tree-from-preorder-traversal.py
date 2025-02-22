# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dashes=0
        stack=[]
        i=0
        while i<len(traversal):
            if traversal[i]=='-':
                dashes+=1
                i+=1
            else:
                j=i
                while j<len(traversal) and traversal[j]!='-':
                    j+=1
                val=int(traversal[i:j])
                node=TreeNode(val)
                while len(stack)>dashes:
                    stack.pop()
                if stack and stack[-1].left==None:
                    stack[-1].left=node
                elif stack:
                    stack[-1].right=node
                stack.append(node)
                i=j
                dashes=0
        return stack[0]

            
