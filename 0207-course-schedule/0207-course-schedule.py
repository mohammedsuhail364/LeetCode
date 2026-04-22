class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
        path=set() # current path
        safe=set() # already check , there is no cycles with this nodes
        def dfs(i):
            if i in path:
                return False
            if i in safe:
                return True
            path.add(i)
            for nei in adj[i]:
                if not dfs(nei): 
                    return False
            path.remove(i)
            safe.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        