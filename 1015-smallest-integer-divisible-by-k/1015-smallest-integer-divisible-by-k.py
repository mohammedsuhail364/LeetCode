class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # refer neetcode
        if k%2==0 or k%5==0:
            return -1
        cur=1
        res=1
        prev=set()
        while cur%k!=0:
            if cur in prev:
                return -1 # cycle detection
            prev.add(cur)
            cur=10*(cur%k)+1
            res+=1
        return res
        
        