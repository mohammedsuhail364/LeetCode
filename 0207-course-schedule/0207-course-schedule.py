class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if i in visit:
                return False
            if adj[i]==[]:
                return True
            visit.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            visit.remove(i)
            adj[i]=[]
            return True
        adj={i:[] for i in range(numCourses)}
        visit=set()
        for i,j in prerequisites:
            adj[i].append(j)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True