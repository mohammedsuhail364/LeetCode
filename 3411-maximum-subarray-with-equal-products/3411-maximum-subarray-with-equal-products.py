class Solution:
    
    
    def maxLength(self, nums: List[int]) -> int:
        def find_gcd(a,b):
            if b==0:return abs(a)
            return find_gcd(b,a%b)
        res = 0
        MAX_VAL = 25200
        # Maximum possible LCM for numbers 1..10 is lcm(1..10) = 2520
        # Maximum possible GCD is 10, so lcm * gcd <= 25200
        for i in range(len(nums)):
            cur_prod = 1
            cur_gcd = 0
            cur_lcm = 1
            for j in range(i,len(nums)):
                cur_prod*=nums[j]
                if cur_prod > MAX_VAL:break
                # to find gcd 
                cur_gcd = find_gcd(cur_gcd,nums[j])
                # to find lcm = (a*b)//gcd(a,b)
                cur_lcm = (cur_lcm*nums[j])//find_gcd(cur_lcm,nums[j])
                if cur_prod == cur_gcd * cur_lcm:
                    res = max(res,j-i+1)
        return res