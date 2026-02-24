class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        for i in nums:
            cur=i
            while stack and math.gcd(stack[-1],cur)>1:
                val=stack.pop()
                cur=math.lcm(val,cur)
            stack.append(cur)
        return stack