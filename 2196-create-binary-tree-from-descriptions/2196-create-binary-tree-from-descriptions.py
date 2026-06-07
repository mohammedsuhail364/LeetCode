# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap={}
        childSet=set()
        for p,c,l in descriptions:
            childSet.add(c)
            if c not in nodeMap:
                nodeMap[c]=TreeNode(c)
            if p not in nodeMap:
                nodeMap[p]=TreeNode(p)
            if l:
                nodeMap[p].left=nodeMap[c]
            else:
                nodeMap[p].right=nodeMap[c]
        for node in nodeMap:
            if node not in childSet:
                return nodeMap[node]
        
        print(nodeMap)
        print(childSet)