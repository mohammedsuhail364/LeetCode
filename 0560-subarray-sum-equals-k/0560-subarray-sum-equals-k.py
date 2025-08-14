class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cursum=0
        res=0
        di={0:1}
        for i in nums:
            cursum+=i
            diff=cursum-k
            if diff in di:
                res+=di[diff]
            if cursum not in di:
                di[cursum]=1
            else:
                di[cursum]+=1
        return res
       