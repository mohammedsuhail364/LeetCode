class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent=list(range(26))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            px,py=find(x),find(y)
            if px!=py:
                if px<py:
                    parent[py]=px
                else:
                    parent[px]=py
        for i,j in zip(s1,s2):
            union(ord(i)-ord('a'),ord(j)-ord('a'))
        res=''
        for i in baseStr:
            root=find(ord(i)-ord('a'))
            res+=(chr(root+ord('a')))
        return res
