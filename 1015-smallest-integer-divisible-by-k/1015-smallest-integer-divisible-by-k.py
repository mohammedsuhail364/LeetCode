class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # refer neetcode
        if k%2==0 or k%5==0:
            return -1
        cur=1
        for res in range(1,k+1):
            if cur%k==0:
                return res
            cur=10*(cur%k)+1
        return -1
        
        