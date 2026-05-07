class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent={}
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return 
            parent[py]=px
        for a,b,c,d in equations:
            if b+c=="==":
                if a not in parent: parent[a]=a
                if d not in parent: parent[d]=d
                union(a,d)
        for a,b,c,d in equations:
            if b+c=="!=":
                if a not in parent: parent[a]=a
                if d not in parent: parent[d]=d
                if find(a)==find(d): # This is correct! Because b!=a says they must be different values, but union-find says they're the same node — contradiction.
                    return False
        return True