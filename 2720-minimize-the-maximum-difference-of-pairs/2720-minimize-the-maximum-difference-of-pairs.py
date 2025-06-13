class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(threshold):
            i=0
            cnt=0
            while i<len(nums)-1:
                if abs(nums[i]-nums[i+1])<=threshold:
                    cnt+=1
                    i+=2
                else:
                    i+=1
                if cnt==p:
                    return True
            return False
        if p==0:return 0
        nums.sort()

        l=0
        r=10**9
        res=10**9
        while l<=r:
            m=(l+r)//2
            if isValid(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
