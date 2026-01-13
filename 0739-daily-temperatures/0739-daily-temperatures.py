class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                idx=stack.pop()
                res[idx]=i-idx
            stack.append(i)
        return res