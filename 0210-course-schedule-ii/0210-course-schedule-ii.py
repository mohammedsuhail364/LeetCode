class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output=[]
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            for nei in adj[i]:
                if not dfs(nei): return False
            cycle.remove(i)
            visit.add(i)
            output.append(i)
            return True
        adj={i:[] for i in range(numCourses)}
        visit=set()
        cycle=set()
        for i,j in prerequisites:
            adj[i].append(j)
        for i in range(numCourses):
            if not dfs(i): return []
        return output