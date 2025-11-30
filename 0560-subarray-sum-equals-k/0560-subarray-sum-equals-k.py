class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        res=0
        seen={0:1}
        cur=0
        for n in nums:
            cur+=n
            rem=cur-k
            if rem in seen:
                res+=seen[rem]
            if cur not in seen:
                seen[cur]=0
            seen[cur]+=1
        return res