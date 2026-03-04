# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        def dfs(node):
            if not node:
                res.append('N')
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        print(res)
        dfs(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=data.split(',')
        index=0
        def dfs():
            nonlocal index
            if data[index]=='N':
                index+=1
                return None
            root=TreeNode(int(data[index]))
            index+=1
            root.left=dfs()
            root.right=dfs()
            return root
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))