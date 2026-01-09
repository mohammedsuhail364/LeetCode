from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for t in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[t]:
                idx=stack.pop()
                res[idx]=t-idx
            stack.append(t)
        return res