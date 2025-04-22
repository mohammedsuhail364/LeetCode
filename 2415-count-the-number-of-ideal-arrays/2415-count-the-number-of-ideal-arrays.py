# \U0001f44e\U0001f44e\U0001f44e\U0001f44e

from collections import Counter
from math import comb
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = maxValue
        freq = {x : 1 for x in range(1, maxValue+1)}
        for k in range(1, n): 
            temp = Counter()
            for x in freq: 
                for m in range(2, maxValue//x+1): 
                    ans += comb(n-1, k)*freq[x]
                    temp[m*x] += freq[x]
            freq = temp
            ans %= 1_000_000_007
        return ans 

# class Solution:
#     def idealArrays(self, n: int, maxValue: int) -> int:
#         self.res=0
#         cache={}
#         MOD=10**9+7
#         def backtrack(li):
#             if len(li)==n:
#                 self.res+=1
#                 return 
#             key=(len(li),li[-1] if li else 0)
#             if key in cache:
#                 self.res+=(cache[key]%MOD)
#                 return 
#             prev_res=self.res
#             for i in range(1,maxValue+1):
#                 if li and i%li[-1]==0:
#                     li.append(i)
#                     backtrack(li)
#                     li.pop()
#                 elif not li:
#                     li.append(i)
#                     backtrack(li)
#                     li.pop()
#             cache[key]=(self.res-prev_res)%MOD
#         backtrack([])
#         return self.res%MOD