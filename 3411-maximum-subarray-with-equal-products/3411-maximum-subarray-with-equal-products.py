class Solution:
    
    
    def maxLength(self, nums: List[int]) -> int:
        def find_gcd(a,b):
            if b==0:return abs(a)
            return find_gcd(b,a%b)
        res = 0
        for i in range(len(nums)):
            cur = 1
            cur_gcd = 0
            cur_lcm = 1
            for j in range(i,len(nums)):
                cur*=nums[j]
                # to find gcd 
                cur_gcd = find_gcd(cur_gcd,nums[j])
                # to find lcm
                cur_lcm = (cur_lcm*nums[j])//find_gcd(cur_lcm,nums[j])
                if cur == cur_gcd * cur_lcm:
                    res = max(res,j-i+1)
        return res