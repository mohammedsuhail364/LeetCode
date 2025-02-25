class Solution:
    def numOfSubarrays(self, arr) -> int:
        res=0
        MOD=10**9+7
        cur_sum=0
        odd=0
        even=0
        for i in arr:
            cur_sum+=i
            if cur_sum%2!=0:
                res+=1
                res+=even
                odd+=1
            else:
                res+=odd
                even+=1
        return res%MOD