class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res=prices[::]
        stack=[]
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                idx=stack.pop()
                res[idx]-=prices[i]
            stack.append(i)
        
        return res