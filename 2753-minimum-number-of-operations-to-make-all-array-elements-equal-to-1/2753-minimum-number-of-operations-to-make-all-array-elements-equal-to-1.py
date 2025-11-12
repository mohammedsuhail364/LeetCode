class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        count_ones=nums.count(1)
        if count_ones>0:
            return n-count_ones
        min_len=inf
        for i in range(n):
            current_gcd=nums[i]
            for j in range(i+1,n):
                current_gcd=math.gcd(current_gcd,nums[j])
                if current_gcd==1:
                    min_len=min(min_len,j-i+1)
                    break
        if min_len==inf:
            return -1
        return (min_len-1)+(n-1)


