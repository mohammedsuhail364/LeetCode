class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        di={}
        res=0
        for i in nums:
            temp=i
            val=0
            while temp:
                val+=temp%10
                temp=temp//10
            if val in di:
                res=max(res,i+di[val])
                di[val]=max(di[val],i)
            else:
                di[val]=i
        return res if res!=0 else -1