class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def findPairsBelowMid(max_dist):
            l=0
            res=0
            for r in range(len(nums)):
                while nums[r]-nums[l]>max_dist:
                    l+=1
                res+=(r-l) # add only valid pairs
            return res
        nums.sort() # important one
        # in this we use the binary search we can take the number and check there is atleast k pairs 
        l=0
        r=nums[-1]-nums[0]

        while l<r:
            m=(l+r)//2
            pairs=findPairsBelowMid(m)
            if pairs>=k:

                r=m
            else:
                l=m+1
        return l