class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        children=defaultdict(list)
        for i in range(1,len(parent)):
            children[parent[i]].append(i)
        last = {}
        new_parent=parent[:]
        def dfs(x):
            c = s[x]
            prev = last.get(c)
            if x!=0 and prev is not None:
                new_parent[x]=prev
            last[c]=x
            for ch in children[x]:dfs(ch)
            # backtrack arrange as old
            if prev is None:
                del last[c]
            else:
                last[c]=prev
        dfs(0)
        new_children=defaultdict(list)
        for i in range(1,n):
            new_children[new_parent[i]].append(i)
        ans=[1]*n
        def size(x):
            for ch in new_children[x]:
                ans[x]+=size(ch)
            return ans[x]
        size(0)
        return ans