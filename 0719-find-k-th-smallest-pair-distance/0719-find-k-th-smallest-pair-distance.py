class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def findPairsBelowM(m):
            l=0
            pairs=0
            for r in range(len(nums)):
                while nums[r]-nums[l]>m:
                    l+=1
                pairs+=(r-l)
            return pairs
        # refer neetcode
        nums.sort()
        l=0
        r=nums[-1]-nums[0]
        while l<r:
            m=l+((r-l)//2)
            if findPairsBelowM(m)>=k:
                r=m
            else:
                l=m+1
        return r