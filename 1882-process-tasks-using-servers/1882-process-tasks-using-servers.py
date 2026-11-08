class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(s,i) for i,s in enumerate(servers)] # (weight,index)
        un_available = [] # (timeFree,weight,index)
        heapify(available)
        t = 0
        res = []
        for i in range(len(tasks)):
            t = max(t,i)
            if not available:t=un_available[0][0] # timeFree
            while un_available and un_available[0][0]<=t:
                timeFree,weight,index = heappop(un_available)
                heappush(available , (weight,index))
            weight,index = heappop(available)
            heappush(un_available,(t+tasks[i],weight,index))
            res.append(index)
        return res