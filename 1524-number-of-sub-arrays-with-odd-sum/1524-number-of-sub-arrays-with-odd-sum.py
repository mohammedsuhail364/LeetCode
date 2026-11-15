class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # odd + odd = even
        # even + odd = odd
        # even + even = even
        MOD = 10**9+7
        even_count = 1
        odd_count = 0
        cur = 0
        res=0
        for x in arr:
            cur = (cur+x)%2
            if cur:
                res += even_count
                odd_count+=1
            else:
                res+=odd_count
                even_count+=1
        return res%MOD