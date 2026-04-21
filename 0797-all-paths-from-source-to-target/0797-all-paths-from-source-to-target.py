class Solution:
    def allPathsSourceTarget(self, graph):

        res=[]
        q=deque([(0,[0])])
        while q:
            node,path=q.popleft()
            if node==len(graph)-1:
                res.append(path)
                continue
            for nei in graph[node]:
                q.append((nei,path+[nei]))
        return res
        
        