class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res=inf
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]==nums[j]==nums[k]:
                        val=abs(i-j)+abs(j-k)+abs(k-i)
                        res=min(res,val)
        return res if res!=inf else -1