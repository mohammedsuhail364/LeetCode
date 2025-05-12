from collections import Counter
import copy
class Solution:
    def findEvenNumbers(self, digits):
        c=Counter(digits)
        digits=set(digits)
        res=[]
        for i in range(100,1000):
            x=copy.deepcopy(c)
            flag=True
            val=i
            while i:
                temp=i%10
                if temp not in digits:
                    flag=False
                    break
                elif x[temp]==0:
                    flag=False
                    break
                x[temp]-=1
                i=i//10
            if flag and val%2==0:
                res.append(val)
        return res
# s=Solution()
# print(s.findEvenNumbers([2,1,3,0]))