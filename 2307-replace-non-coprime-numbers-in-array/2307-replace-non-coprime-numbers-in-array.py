import math
class Solution:
    def replaceNonCoprimes(self, nums) :
        stack=[]
        for i in nums:
            curr=i
            while stack and math.gcd(stack[-1],curr)>1:
                curr=math.lcm(curr,stack.pop())
            stack.append(curr)
        return stack