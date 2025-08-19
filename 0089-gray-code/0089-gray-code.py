class Solution:
    def grayCode(self, n: int) -> List[int]:
        def convert(nums):
            res=[]
            for i in nums:
                res.append(int(i,2))
            return res
        val=['0','1']
        if n==1:
            return convert(val)
        for i in range(n-1):
            tmp=val
            tmp1=val[::-1]
            for x in range(len(tmp)):
                tmp[x]='0'+tmp[x]
            for x in range(len(tmp1)):
                tmp1[x]='1'+tmp1[x]
            val=tmp+tmp1
        return convert(val)
