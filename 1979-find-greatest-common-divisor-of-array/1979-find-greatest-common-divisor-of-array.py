class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def find_gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        return find_gcd(min(nums),max(nums))