class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=0
        r=l+3
        res=[]
        while r<len(num)+1:
            val=num[l:r]
            if len(set(val))==1:
                res.append(val)
            l+=1
            r+=1
        return max(res) if res else ""