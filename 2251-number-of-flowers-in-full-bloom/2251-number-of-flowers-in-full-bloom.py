class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # can we solve with two different approach 
        # 1. using heap -> refer neetcode
        # 2. using sweep line -> refer editorial
        diff={} # default case we see 0 new flowers at 0 time
        def getRightMostElement(nums,target):
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                m=(l+r)//2
                if nums[m]<=target:
                    res=m
                    l=m+1
                else:
                    r=m-1
            return res

        for s,e in flowers:
            diff[s]=diff.get(s,0)+1
            diff[e+1]=diff.get(e+1,0)-1

        prefix=[]
        positions=[]
        cur=0
        for key,val in sorted(diff.items()):
            positions.append(key)
            cur+=val
            prefix.append(cur)
        res=[]
        for p in people:
            idx=getRightMostElement(positions,p)
            if idx==-1:
                res.append(0)
            else:
                res.append(prefix[idx])
        return res

        