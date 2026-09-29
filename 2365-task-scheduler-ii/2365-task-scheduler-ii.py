class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        lastSeen={}
        res=0
        for i in tasks:
            res+=1
            if i in lastSeen:
                lastWork = lastSeen[i]
                if (res - lastWork)<=space:
                    res=lastWork+space+1
            lastSeen[i]=res
        return res