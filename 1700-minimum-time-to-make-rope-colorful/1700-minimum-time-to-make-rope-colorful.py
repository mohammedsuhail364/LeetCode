class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res=0
        prev=0
        for i in range(1,len(colors)):
            if colors[prev]==colors[i]:
                res+=(min(neededTime[prev],neededTime[i]))
                if neededTime[i]>neededTime[prev]:
                    prev=i
            else:
                prev=i
        return res