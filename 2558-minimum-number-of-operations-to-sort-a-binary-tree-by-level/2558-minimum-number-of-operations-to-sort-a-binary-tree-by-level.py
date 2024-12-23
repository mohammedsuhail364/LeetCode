# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        all_level = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            all_level.append(level)

        res = 0
        res = 0
        for x in all_level:
            if len(x) == 1:
                continue
            x1 = sorted(x)
            dic = {}
            for i, val in enumerate(x):
                dic[val] = i
            i = 0
            j = 0
            while i < len(x) and j < len(x1):
                if x[i] == x1[j]:
                    i += 1
                    j += 1
                else:
                    index = dic[x1[j]]

                    res += 1
                    x[i], x[index] = x[index], x[i]
                    dic[x[index]] = index
                    i += 1
                    j += 1
        return res
